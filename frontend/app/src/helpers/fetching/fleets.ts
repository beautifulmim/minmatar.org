import { useTranslations } from '@i18n/utils';
const t = useTranslations('en');

import type {
    FleetUI,
    FleetItem,
    DoctrineType,
    FleetCompositionUI,
    FleetRadarUI,
    CharacterBasic,
    Locales,
    FleetTrackingTexts,
} from '@dtypes/layout_components'
import type { EveCharacterProfile, Fleet, FleetMember, FleetBasic } from '@dtypes/api.minmatar.org'
import { get_fleets_v3, get_fleets_v2, get_fleet_by_id } from '@helpers/api.minmatar.org/fleets'
import { get_route } from '@helpers/api.eveonline/routes'
import { get_user_character, get_users_character } from '@helpers/fetching/characters'
import { fetch_doctrine_by_id } from '@helpers/fetching/doctrines'
import { get_system_sun_type_id } from '@helpers/sde/map'
import { get_fleet_users } from '@helpers/api.minmatar.org/fleets'
import { unique_values } from '@helpers/array'
import { time_diff_text } from '@helpers/date'

const SOSALA_SYSTEM_ID = 30003070
const DEFAULT_STAGGERING_SYSTEM = SOSALA_SYSTEM_ID

export async function fetch_fleets_auth(access_token:string, upcoming:boolean = true) {
    let api_fleets:Fleet[]

    api_fleets = await get_fleets_v3(access_token, upcoming ? 'active' : 'recent')
    api_fleets = api_fleets.filter(api_fleet => api_fleet.fleet_commander)
    if (!upcoming)
        api_fleets = api_fleets.filter(api_fleet => api_fleet?.tracking || new Date(api_fleet.start_time) < new Date())
    
    const fleet_commanders = unique_values(api_fleets.map(api_fleet => api_fleet.fleet_commander))
    const fleet_commanders_profiles = await get_users_character(fleet_commanders)

    return api_fleets.map( fleet => add_fleet_info(fleet, fleet_commanders_profiles.find(profile => profile?.user_id === fleet?.fleet_commander)) )
}

export async function fetch_fleets(upcoming:boolean = true) {
    let api_fleets_id:FleetBasic[]

    api_fleets_id = await get_fleets_v2(upcoming)

    return api_fleets_id.map((api_fleet) => {
        return {
            id: api_fleet.id,
            audience: api_fleet.audience,
            fleet_commander_id: 0,
            fleet_commander_name: t('not_available'),
            start_time: new Date('2100-01-01'),
        } as FleetItem
    } )
}

export function add_fleet_info(fleet:Fleet, fc_profile:EveCharacterProfile | undefined) {
    return {
        id: fleet.id,
        description: fleet.description,
        audience: fleet.audience,
        doctrine_id: fleet.doctrine_id,
        fleet_commander_id: fc_profile?.character_id ?? 0,
        fleet_commander_name: fc_profile?.character_name ?? t('not_available'),
        location: fleet.location,
        start_time: fleet.start_time,
        type: fleet.type,
        tracking: fleet.tracking,
        status: fleet.status,
    } as FleetItem
}

export async function fetch_fleet_by_id(access_token:string, fleet_id:number) {
    const fleet = await get_fleet_by_id(access_token, fleet_id)
        
    let character_profile:EveCharacterProfile | null = null
    if (fleet?.fleet_commander)
        character_profile = await get_user_character(fleet.fleet_commander)

    let doctrine:DoctrineType | null = null
    if (fleet?.doctrine_id)
        doctrine = await fetch_doctrine_by_id(fleet.doctrine_id)

    return {
        id: fleet.id,
        description: fleet.description,
        fleet_commander_id: character_profile?.character_id ?? 0,
        fleet_commander_name: character_profile?.character_name ?? t('unknown_character'),
        location: fleet.location,
        start_time: fleet.start_time,
        type: fleet.type,
        doctrine: fleet?.doctrine_id ? doctrine : null,
        tracking: fleet.tracking,
        audience: fleet.audience,
        disable_motd: fleet.disable_motd,
        status: fleet.status,
    } as FleetUI
}

export function group_members_by_ship(members:FleetMember[]):FleetCompositionUI[] {
    const ship_type_ids = [...new Set(members.map(member => member.ship_type_id))];

    return ship_type_ids.map((ship_type_id) => {
        const filtered_members = members.filter((member) => member.ship_type_id === ship_type_id)

        return {
            ship_type_id: ship_type_id,
            ship_type_name: filtered_members[0].ship_type_name,
            members: filtered_members.map((member):CharacterBasic => {
                return {
                    character_id: member.character_id,
                    character_name: member.character_name
                }
            })
        } as FleetCompositionUI
    })
}

export async function group_members_by_location(members:FleetMember[], staging_solar_system_id:number = DEFAULT_STAGGERING_SYSTEM) {
    const solar_system_ids = [...new Set(members.map(member => member.solar_system_id))];

    return await Promise.all(solar_system_ids.map(async (solar_system_id) => {
        const filtered_members = members.filter((member) => member.solar_system_id === solar_system_id)
        const route = await get_route(solar_system_id, staging_solar_system_id)

        return {
            solar_system_id: solar_system_id,
            solar_system_name: filtered_members[0].solar_system_name,
            start_type_id: await get_system_sun_type_id(solar_system_id),
            jumps: route.length - 1,
            members: filtered_members.map((member):CharacterBasic => {
                return {
                    character_id: member.character_id,
                    character_name: member.character_name
                }
            })
        } as FleetRadarUI
    })) as FleetRadarUI[]
}

export async function fetch_fleet_users(fleet_id:number) {
    const fleet_users = await get_fleet_users(fleet_id)
        
    if (fleet_users?.length > 0) {
        return fleet_users.find(() => true)?.user_ids
    }

    return []
}

export function get_fleet_tracking_texts(locale:Locales = 'en', fleet:FleetUI): FleetTrackingTexts | false {
    try {
        const t = useTranslations(locale)

        if (fleet?.tracking?.end_time) {
            const fleet_start_eve_time = new Date(fleet.tracking.start_time)
            const fleet_end_eve_time = new Date(fleet.tracking.end_time)
            const fleet_start_eve_time_text = fleet_start_eve_time.toLocaleDateString(locale, JSON.parse(import.meta.env.DATETIME_FORMAT))
            const fleet_end_eve_time_text = fleet_end_eve_time.toLocaleDateString(locale, JSON.parse(import.meta.env.DATETIME_FORMAT))
            const fleet_tracking_hint = t('fleet_tracking_hint').replace('FLEET_START', fleet_start_eve_time_text).replace('FLEET_END', fleet_end_eve_time_text)
            const fleet_duration_text = time_diff_text(locale, fleet.tracking.start_time, fleet.tracking.end_time)

            return {
                fleet_end_eve_time_text: fleet_end_eve_time_text,
                fleet_duration_text: fleet_duration_text,
                fleet_tracking_hint: fleet_tracking_hint,
            } as FleetTrackingTexts
        }
    } catch (error) {
        console.log(error)
    }

    return false
}
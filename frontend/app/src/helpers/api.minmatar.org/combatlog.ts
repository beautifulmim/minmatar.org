import type { CombatLog } from '@dtypes/api.minmatar.org'
import { get_error_message, query_string } from '@helpers/string'

const API_ENDPOINT =  `${import.meta.env.API_URL}/api/combatlog`

export async function analize_log(combatlog:string) {
    const headers = {
        'Content-Type': 'text/plain'
    }

    const ENDPOINT = `${API_ENDPOINT}/`

    console.log(`Requesting POST: ${ENDPOINT}`)

    try {
        const response = await fetch(ENDPOINT, {
            headers: headers,
            body: combatlog,
            method: 'POST'
        })

        // console.log(response)

        if (!response.ok) {
            throw new Error(get_error_message(
                response.status,
                `POST ${ENDPOINT}`
            ))
        }

        return await response.json() as CombatLog;
    } catch (error) {
        throw new Error(`Error analizing log: ${error.message}`);
    }
}

export async function analize_zipped_log(combatlog:Uint8Array, fitting_id?:number, fleet_id?:number) {
    const headers = {
        'Content-Type': 'application/gzip',
    }

    const optional_attributes = {
        ...((fitting_id !== undefined && fitting_id > 0) && { "fitting_id": fitting_id }),
        ...((fleet_id !== undefined && fleet_id > 0) && { "fleet_id": fleet_id }),
    }

    const query = query_string(optional_attributes)

    const ENDPOINT = `${API_ENDPOINT}${query ? `?${query}` : query}`

    console.log(`Requesting POST: ${ENDPOINT}`)

    try {
        const response = await fetch(ENDPOINT, {
            headers: headers,
            body: combatlog,
            method: 'POST'
        })

        // console.log(response)

        if (!response.ok) {
            throw new Error(get_error_message(
                response.status,
                `POST ${ENDPOINT}`
            ))
        }

        return await response.json() as CombatLog;
    } catch (error) {
        throw new Error(`Error analizing log: ${error.message}`);
    }
}
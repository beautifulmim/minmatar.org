from django.db.models import signals
from django.dispatch import receiver

from fleets.models import EveFleet
from fleets.tasks import update_fleet_schedule


@receiver(signals.post_save, sender=EveFleet)
def update_fleet_schedule_on_save(sender, instance, created, **kwargs):
    if created:
        update_fleet_schedule()
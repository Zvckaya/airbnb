from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    def handle(self, *args, **options):
        amenities = [
            "bClean linens",
            "Toilet paper",
            "Towels",
            "WiFi with passwords clearly displayed",
            "Iron with (full-sized) ironing board",
            "Universal charging station",
            "One key per bedroom",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenitiescreated"))

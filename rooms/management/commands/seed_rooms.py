from django.core.management.base import BaseCommand
import random
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "this command creates users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many youser you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guest": lambda x: random.randint(0, 20),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        create_photos = seeder.execute()
        created_clean = flatten(list(create_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouserRule.objects.all()

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,33)}.webp",
                )
        for a in amenities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.amenities.add(a))
        
        for f in facilities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.facilities.add(a)
        
        for r in rules:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.HouserRule.add(a)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))


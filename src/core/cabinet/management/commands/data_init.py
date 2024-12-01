from django.core.management.base import BaseCommand
from django.db import transaction

from dispatcher.models import City, CostPerKm, CostPerBabyChair

class Command(BaseCommand):
    """Django command to create a default city if none exists"""

    def handle(self, *args, **options):
        if not City.objects.exists():
            self.create_default_city()

    def create_default_city(self):
        """Creates a default city"""
        with transaction.atomic():
            cost_per_km = CostPerKm.objects.create(
                value=25,  # Используйте 'value' вместо 'cost'
                night_allowance=15
            )

            cost_per_baby_chair = CostPerBabyChair.objects.create(
                value=25,  # Используйте 'value' вместо 'cost'
                night_allowance=15
            )

            City.objects.create(
                name="Москва",
                minimal_cost=50,
                timezone="Europe/Moscow",
                cost_per_km=cost_per_km,
                cost_per_baby_chair=cost_per_baby_chair,
                search_drivers_radius=5000  # или другое значение по умолчанию
            )

            self.stdout.write(self.style.SUCCESS('Default city created successfully!'))
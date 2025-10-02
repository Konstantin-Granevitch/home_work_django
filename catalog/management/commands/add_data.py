from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Add test data in Product & Category"

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'category_fixture.json') # загрузка данных в категории
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

        call_command('loaddata', 'product_fixture.json') # загрузка данных в продукты
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
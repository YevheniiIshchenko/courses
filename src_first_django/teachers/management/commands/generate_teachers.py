import random

from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher

fake = Faker('uk_UA')
stups = ['professor', 'docent', 'assistant']


class Command(BaseCommand):
    args = ['count']

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, default=100)

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                stupen=random.choice(stups)
            )

from django.core.management.base import BaseCommand

import kronos


@kronos.register('0 0 * * *')
class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Hello, world!')
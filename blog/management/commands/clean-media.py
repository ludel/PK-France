import os

from django.conf import settings
from django.core.management.base import BaseCommand

from blog.models import Fact, News


class Command(BaseCommand):
    help = 'Delete unused media'

    def add_arguments(self, parser):
        parser.add_argument('dir_name', type=str)

    def handle(self, *args, **options):
        models = {
            'fact': Fact.objects.values('image'),
            'article': News.objects.values('image_min', 'image_max')
        }

        dir_name = options['dir_name']
        all_files = set(os.listdir(f'{settings.MEDIA_ROOT}/{dir_name}'))
        used_files = set()

        for field_names in models[dir_name]:
            for name in field_names.values():
                used_files.add(name.replace(f'{dir_name}/', ''))

        for file in all_files.difference(used_files):
            print(f'=> removing {file}')
            os.remove(f'{settings.MEDIA_ROOT}/{dir_name}/{file}')

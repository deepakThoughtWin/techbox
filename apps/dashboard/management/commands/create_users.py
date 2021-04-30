from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        self.stdout.write(self.style.HTTP_SERVER_ERROR(f'Initializing {total} Users creation.....'))
        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                user=User.objects.create_superuser(username=username, email='', password='123')
                self.stdout.write(self.style.SUCCESS('User "%s (%s)" Superuser Created with success!' % (user.username,user.id)))
            else:
                user=User.objects.create_user(username=username, email='', password='123')
                self.stdout.write(self.style.SUCCESS('User "%s (%s)" Created with success!' % (user.username,user.id)))

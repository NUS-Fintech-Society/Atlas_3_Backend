from django.core.management import BaseCommand
from django.contrib.auth.models import User

from random import choice

from authentication.models import AtlasUser


class Command(BaseCommand):
    help = "Populates the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--verbose",
            action="store_const",
            const=True,
            default=False,
            help="Provide verbose output when seeding the database",
        )

    def create_users(self, verbose=False):
        User.objects.all().delete()
        AtlasUser.objects.all().delete()

        user = User.objects.create_superuser("admin", "admin@example.com", "password")
        user.save()
        admin_profile = AtlasUser(user=user, department=choice(list(AtlasUser.DepartmentNames)), role=AtlasUser.Roles.ADMIN)
        admin_profile.save()

        if verbose:
            self.stdout.write(f"Created superuser {user.username} {user.email}")
            self.stdout.write(f"Created admin profile {admin_profile}")
        for i in range(5):
            user = User.objects.create_user(
                f"user{i + 1}", f"user{i + 1}@example.com", "password"
            )
            user.save()
            profile = AtlasUser(user=user, department=choice(list(AtlasUser.DepartmentNames)))
            profile.save()
            if verbose:
                self.stdout.write(f"Created user {user.username} {user.email}")
                self.stdout.write(f"Created profile {profile}")

    def handle(self, *args, **options):
        self.stdout.write("Populating database...")

        self.create_users(verbose=options["verbose"])

        self.stdout.write(self.style.SUCCESS("Successfully populated database"))

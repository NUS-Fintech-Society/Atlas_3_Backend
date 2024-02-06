from django.core.management import BaseCommand
from django.contrib.auth.models import User


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
        user = User.objects.create_superuser("admin", "admin@example.com", "password")
        user.save()

        if verbose:
            self.stdout.write(f"Created superuser {user.username} {user.email}")
        for i in range(1, 6):
            user = User.objects.create_user(
                f"user{i}", f"user{i}@example.com", "password"
            )
            user.save()
            if verbose:
                self.stdout.write(f"Created user {user.username} {user.email}")

    def handle(self, *args, **options):
        self.stdout.write("Populating database...")

        self.create_users(verbose=options["verbose"])

        self.stdout.write(self.style.SUCCESS("Successfully populated database"))

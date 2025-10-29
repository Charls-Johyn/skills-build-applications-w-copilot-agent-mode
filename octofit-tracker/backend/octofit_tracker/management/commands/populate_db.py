from django.core.management.base import BaseCommand
from octofit_tracker.models import UserProfile, Team, Activity, Workout, LeaderboardEntry


class Command(BaseCommand):
    help = "Populate the octofit_db with sample data for development/testing."

    def handle(self, *args, **options):
        # Create sample users (use get_or_create so it's idempotent)
        alice, _ = UserProfile.objects.get_or_create(email="alice@example.com", defaults={"name": "Alice"})
        bob, _ = UserProfile.objects.get_or_create(email="bob@example.com", defaults={"name": "Bob"})

        # Create a team. Avoid ManyToMany.add to sidestep djongo ObjectId vs int issues.
        team, _ = Team.objects.get_or_create(name="Team Alpha")

        # Create activities using foreign key id fields to avoid unsaved-related-object checks
        Activity.objects.get_or_create(user_id=alice.pk, activity_type="running", duration_minutes=30)
        Activity.objects.get_or_create(user_id=bob.pk, activity_type="cycling", duration_minutes=45)

        # Create a simple workout
        Workout.objects.get_or_create(title="Morning Blast", defaults={"description": "Short cardio routine"})

        # Create leaderboard entry using team_id
        LeaderboardEntry.objects.get_or_create(team_id=team.pk, defaults={"points": 100})

        self.stdout.write(self.style.SUCCESS("Sample data created/verified in octofit_db"))

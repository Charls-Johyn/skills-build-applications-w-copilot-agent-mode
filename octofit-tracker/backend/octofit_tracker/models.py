from django.db import models


class UserProfile(models.Model):
    """Simple user profile for demo/testing."""
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"


class Team(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(UserProfile, related_name="teams", blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} by {self.user.name} ({self.duration_minutes}m)"


class Workout(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    activities = models.ManyToManyField(Activity, related_name="workouts", blank=True)

    def __str__(self):
        return self.title


class LeaderboardEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="leaderboard_entries")
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name}: {self.points} pts"

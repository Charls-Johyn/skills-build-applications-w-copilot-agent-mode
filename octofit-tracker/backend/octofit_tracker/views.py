from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter

from .models import UserProfile, Team, Activity, Workout, LeaderboardEntry
from .serializers import (
    UserProfileSerializer,
    TeamSerializer,
    ActivitySerializer,
    WorkoutSerializer,
    LeaderboardEntrySerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer


router = DefaultRouter()
router.register(r"users", UserProfileViewSet)
router.register(r"teams", TeamViewSet)
router.register(r"activities", ActivityViewSet)
router.register(r"workouts", WorkoutViewSet)
router.register(r"leaderboard", LeaderboardEntryViewSet)


@api_view(["GET"])
def api_root(request):
    """Simple API root that points to the router endpoints."""
    data = {"api": request.build_absolute_uri("api/")}
    return Response(data)

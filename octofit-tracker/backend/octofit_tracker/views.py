from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from octofit_tracker.serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)

User = get_user_model()


@api_view(['GET'])
def api_root(request):
    """API root view"""
    return Response({
        'users': request.build_absolute_uri('/api/users/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
        'workouts': request.build_absolute_uri('/api/workouts/'),
    })


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for User model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for Team model"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for Activity model"""
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        """Filter activities by user if provided"""
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """ViewSet for Leaderboard model"""
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        """Filter leaderboard by team if provided"""
        queryset = Leaderboard.objects.all().order_by('rank')
        team_id = self.request.query_params.get('team_id', None)
        if team_id is not None:
            queryset = queryset.filter(team_id=team_id)
        return queryset


class WorkoutViewSet(viewsets.ModelViewSet):
    """ViewSet for Workout model"""
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        """Filter workouts by difficulty if provided"""
        queryset = Workout.objects.all()
        difficulty = self.request.query_params.get('difficulty', None)
        if difficulty is not None:
            queryset = queryset.filter(difficulty_level=difficulty)
        return queryset

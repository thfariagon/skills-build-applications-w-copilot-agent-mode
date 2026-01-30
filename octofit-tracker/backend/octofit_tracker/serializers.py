from rest_framework import serializers
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'bio', 'avatar_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    id = serializers.CharField(read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'logo_url', 'members', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True, source='user.id')

    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration_minutes', 'distance_km', 'calories_burned', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    team_id = serializers.CharField(read_only=True, source='team.id')

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'team_id', 'total_calories', 'total_duration', 'total_distance', 'rank', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'difficulty_level', 'duration_minutes', 'exercise_type', 'instructions', 'equipment_needed', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """User model for OctoFit Tracker"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        managed = True

    def __str__(self):
        return self.username


class Team(models.Model):
    """Team model for OctoFit Tracker"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    logo_url = models.URLField(blank=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'
        managed = True

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for OctoFit Tracker"""
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('gym', 'Gym'),
        ('yoga', 'Yoga'),
        ('walking', 'Walking'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(default=0)
    calories_burned = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'
        managed = True

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class Leaderboard(models.Model):
    """Leaderboard model for OctoFit Tracker"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_entry')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries')
    total_calories = models.BigIntegerField(default=0)
    total_duration = models.BigIntegerField(default=0)
    total_distance = models.FloatField(default=0)
    rank = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'
        managed = True
        unique_together = ('user', 'team')

    def __str__(self):
        return f"{self.user.username} - Rank {self.rank}"


class Workout(models.Model):
    """Workout model for OctoFit Tracker"""
    DIFFICULTY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50, choices=DIFFICULTY_LEVELS)
    duration_minutes = models.IntegerField()
    exercise_type = models.CharField(max_length=50)
    instructions = models.TextField()
    equipment_needed = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'
        managed = True

    def __str__(self):
        return self.title

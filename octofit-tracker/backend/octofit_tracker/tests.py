from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')

    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='teamuser', email='team@example.com', password='testpass')
        self.team = Team.objects.create(name='Team A')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(self.team.name, 'Team A')

    def test_get_teams(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='activityuser', email='activity@example.com', password='testpass')
        self.activity = Activity.objects.create(user=self.user, activity_type='running', duration_minutes=30)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.activity_type, 'running')

    def test_get_activities(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(title='Morning Run', description='A quick run', difficulty_level='beginner', duration_minutes=20, exercise_type='running', instructions='Run fast', equipment_needed='None')

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(self.workout.title, 'Morning Run')

    def test_get_workouts(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='leaderuser', email='leader@example.com', password='testpass')
        self.team = Team.objects.create(name='Team B')
        self.leaderboard = Leaderboard.objects.create(user=self.user, team=self.team)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard.user, self.user)

    def test_get_leaderboard(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

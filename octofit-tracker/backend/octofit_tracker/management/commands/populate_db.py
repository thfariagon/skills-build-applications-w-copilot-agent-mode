from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random

User = get_user_model()

# Superhero data - Marvel Team
MARVEL_HEROES = [
    {
        'username': 'iron_man',
        'email': 'tony.stark@marvel.com',
        'first_name': 'Tony',
        'last_name': 'Stark',
    },
    {
        'username': 'captain_america',
        'email': 'steve.rogers@marvel.com',
        'first_name': 'Steve',
        'last_name': 'Rogers',
    },
    {
        'username': 'thor',
        'email': 'thor.odinson@marvel.com',
        'first_name': 'Thor',
        'last_name': 'Odinson',
    },
    {
        'username': 'black_widow',
        'email': 'natasha.romanoff@marvel.com',
        'first_name': 'Natasha',
        'last_name': 'Romanoff',
    },
]

# Superhero data - DC Team
DC_HEROES = [
    {
        'username': 'batman',
        'email': 'bruce.wayne@dc.com',
        'first_name': 'Bruce',
        'last_name': 'Wayne',
    },
    {
        'username': 'superman',
        'email': 'clark.kent@dc.com',
        'first_name': 'Clark',
        'last_name': 'Kent',
    },
    {
        'username': 'wonder_woman',
        'email': 'diana.prince@dc.com',
        'first_name': 'Diana',
        'last_name': 'Prince',
    },
    {
        'username': 'the_flash',
        'email': 'barry.allen@dc.com',
        'first_name': 'Barry',
        'last_name': 'Allen',
    },
]

ACTIVITIES = [
    {'activity_type': 'running', 'duration_minutes': 45, 'distance_km': 8.5, 'calories_burned': 600},
    {'activity_type': 'cycling', 'duration_minutes': 60, 'distance_km': 25.0, 'calories_burned': 450},
    {'activity_type': 'swimming', 'duration_minutes': 40, 'distance_km': 2.0, 'calories_burned': 400},
    {'activity_type': 'gym', 'duration_minutes': 75, 'distance_km': 0, 'calories_burned': 500},
    {'activity_type': 'yoga', 'duration_minutes': 60, 'distance_km': 0, 'calories_burned': 300},
    {'activity_type': 'walking', 'duration_minutes': 30, 'distance_km': 3.0, 'calories_burned': 150},
]

WORKOUTS = [
    {
        'title': 'Morning Run',
        'description': 'A refreshing morning run to start your day',
        'difficulty_level': 'beginner',
        'duration_minutes': 30,
        'exercise_type': 'running',
        'instructions': 'Start with a warm-up walk for 5 minutes, then run at a steady pace for 25 minutes.',
        'equipment_needed': 'Running shoes, sports watch',
    },
    {
        'title': 'Advanced HIIT Workout',
        'description': 'High-intensity interval training for maximum calorie burn',
        'difficulty_level': 'advanced',
        'duration_minutes': 45,
        'exercise_type': 'gym',
        'instructions': 'Perform 30 seconds of maximum effort followed by 30 seconds of rest. Repeat 15 times.',
        'equipment_needed': 'Gym equipment, timer',
    },
    {
        'title': 'Yoga Flow',
        'description': 'Relaxing yoga session for flexibility and mindfulness',
        'difficulty_level': 'beginner',
        'duration_minutes': 60,
        'exercise_type': 'yoga',
        'instructions': 'Follow the instructor through various asanas focusing on breathing and alignment.',
        'equipment_needed': 'Yoga mat, yoga blocks',
    },
    {
        'title': 'Cycling Challenge',
        'description': 'Mountain biking adventure with challenging terrain',
        'difficulty_level': 'intermediate',
        'duration_minutes': 90,
        'exercise_type': 'cycling',
        'instructions': 'Navigate through mountain trails, maintaining a steady pace with focus on technique.',
        'equipment_needed': 'Mountain bike, helmet, water bottle',
    },
    {
        'title': 'Swimming Drills',
        'description': 'Structured swimming session with various stroke drills',
        'difficulty_level': 'intermediate',
        'duration_minutes': 50,
        'exercise_type': 'swimming',
        'instructions': 'Perform front crawl, backstroke, and breaststroke in 10-minute intervals.',
        'equipment_needed': 'Swimming goggles, swimming cap, kickboard',
    },
]


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='The Marvel Cinematic Universe heroes',
            logo_url='https://example.com/marvel-logo.png',
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='The DC Universe heroes',
            logo_url='https://example.com/dc-logo.png',
        )

        # Create Marvel users
        self.stdout.write('Creating Marvel superheroes...')
        marvel_users = []
        for hero_data in MARVEL_HEROES:
            user = User.objects.create_user(
                username=hero_data['username'],
                email=hero_data['email'],
                first_name=hero_data['first_name'],
                last_name=hero_data['last_name'],
                password='superheropwd123'
            )
            team_marvel.members.add(user)
            marvel_users.append(user)

        # Create DC users
        self.stdout.write('Creating DC superheroes...')
        dc_users = []
        for hero_data in DC_HEROES:
            user = User.objects.create_user(
                username=hero_data['username'],
                email=hero_data['email'],
                first_name=hero_data['first_name'],
                last_name=hero_data['last_name'],
                password='superheropwd123'
            )
            team_dc.members.add(user)
            dc_users.append(user)

        # Create activities for each user
        self.stdout.write('Creating activities...')
        all_users = marvel_users + dc_users
        for user in all_users:
            for _ in range(random.randint(3, 8)):
                activity_data = random.choice(ACTIVITIES)
                Activity.objects.create(
                    user=user,
                    activity_type=activity_data['activity_type'],
                    duration_minutes=activity_data['duration_minutes'],
                    distance_km=activity_data['distance_km'],
                    calories_burned=activity_data['calories_burned'],
                    description=f"Activity by {user.first_name} {user.last_name}",
                )

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        rank = 1
        for user in marvel_users + dc_users:
            activities = Activity.objects.filter(user=user)
            total_calories = sum(a.calories_burned for a in activities)
            total_duration = sum(a.duration_minutes for a in activities)
            total_distance = sum(a.distance_km for a in activities)
            
            team = team_marvel if user in marvel_users else team_dc
            
            Leaderboard.objects.create(
                user=user,
                team=team,
                total_calories=total_calories,
                total_duration=total_duration,
                total_distance=total_distance,
                rank=rank,
            )
            rank += 1

        # Create workouts
        self.stdout.write('Creating workouts...')
        for workout_data in WORKOUTS:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} users'))
        self.stdout.write(self.style.SUCCESS(f'Created 2 teams'))
        self.stdout.write(self.style.SUCCESS(f'Created {Activity.objects.count()} activities'))
        self.stdout.write(self.style.SUCCESS(f'Created {Leaderboard.objects.count()} leaderboard entries'))
        self.stdout.write(self.style.SUCCESS(f'Created {Workout.objects.count()} workouts'))

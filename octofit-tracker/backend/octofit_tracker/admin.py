from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'bio', 'avatar_url')}),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('members',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'calories_burned', 'created_at')
    list_filter = ('activity_type', 'created_at')
    search_fields = ('user__username',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'rank', 'total_calories', 'total_duration')
    list_filter = ('team', 'rank')
    search_fields = ('user__username',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty_level', 'exercise_type', 'duration_minutes')
    list_filter = ('difficulty_level', 'exercise_type')
    search_fields = ('title',)

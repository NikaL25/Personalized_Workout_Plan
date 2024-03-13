# workouts/serializers.py
from rest_framework import serializers
from .models import WorkoutPlan, WeightTracking, FitnessGoal, WorkoutSession, CompletedExercise

class WorkoutPlanSerializer(serializers.ModelSerializer):
    session_duration = serializers.DurationField(read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'frequency', 'goals', 'session_duration', 'exercises']

class WeightTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightTracking
        fields = ['id', 'date', 'weight']

class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = ['id', 'weight_objective', 'exercise_achievement']

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['id', 'user', 'start_time', 'end_time']

class CompletedExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedExercise
        fields = ['id', 'workout_session', 'exercise', 'sets_completed', 'repetitions_completed', 'notes']

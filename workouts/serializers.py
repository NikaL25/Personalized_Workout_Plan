from rest_framework import serializers
from .models import WorkoutPlan, WorkoutSession

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = '__all__'

class WorkoutPlanSerializer(serializers.ModelSerializer):
    sessions = WorkoutSessionSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = '__all__'

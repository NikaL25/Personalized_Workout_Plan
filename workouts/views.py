# workouts/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import WorkoutPlan, WeightTracking, FitnessGoal, WorkoutSession, CompletedExercise
from .serializers import (
    WorkoutPlanSerializer,
    WeightTrackingSerializer,
    FitnessGoalSerializer,
    WorkoutSessionSerializer,
    CompletedExerciseSerializer
)

class WorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

class WeightTrackingViewSet(viewsets.ModelViewSet):
    queryset = WeightTracking.objects.all()
    serializer_class = WeightTrackingSerializer
    permission_classes = [IsAuthenticated]

class FitnessGoalViewSet(viewsets.ModelViewSet):
    queryset = FitnessGoal.objects.all()
    serializer_class = FitnessGoalSerializer
    permission_classes = [IsAuthenticated]

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    permission_classes = [IsAuthenticated]

class CompletedExerciseViewSet(viewsets.ModelViewSet):
    queryset = CompletedExercise.objects.all()
    serializer_class = CompletedExerciseSerializer
    permission_classes = [IsAuthenticated]

from django.contrib import admin
from .models import WorkoutPlan, WeightTracking, FitnessGoal, CompletedExercise
# Register your models here.

admin.site.register(WorkoutPlan)
admin.site.register(WeightTracking)
admin.site.register(FitnessGoal)
admin.site.register(CompletedExercise)
from django.contrib import admin
from .models import WorkoutPlan, WorkoutSession


admin.site.register(WorkoutPlan)
admin.site.register(WorkoutSession)

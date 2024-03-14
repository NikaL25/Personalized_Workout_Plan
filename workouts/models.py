from django.db import models
from django.contrib.auth import get_user_model
from exercises.models import Exercise

User = get_user_model()

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50)
    goals = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Workout Plan for {self.user.username}"

class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()
    duration = models.IntegerField()  # Change to IntegerField
    distance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Workout Session for {self.workout_plan.user.username} - {self.exercise.name}"

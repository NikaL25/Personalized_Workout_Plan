# workouts/models.py
from django.db import models
from django.contrib.auth import get_user_model
from exercises.models import Exercise

User = get_user_model()

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    goals = models.CharField(max_length=100)  
    session_duration = models.DurationField()  

    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return self.name

class WeightTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight_objective = models.DecimalField(max_digits=5, decimal_places=2)
    exercise_achievement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Fitness Goal"

class CompletedExercise(models.Model):
    workout_session = models.ForeignKey('WorkoutSession', on_delete=models.CASCADE)  # Corrected reference to WorkoutSession model
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets_completed = models.PositiveIntegerField()
    repetitions_completed = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.exercise} - Sets: {self.sets_completed}, Reps: {self.repetitions_completed}"
# workouts/models.py




class WorkoutSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Workout Session for {self.user.username}"
    
class WorkoutExercise(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.workout_plan.name} - {self.exercise.name}"

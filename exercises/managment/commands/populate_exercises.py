# exercises/management/commands/populate_exercises.py
from django.core.management.base import BaseCommand
from exercises.models import Exercise

class Command(BaseCommand):
    help = 'Populate the database with initial exercises'

    def handle(self, *args, **options):
        exercises_data = [ 
            
        {'name': 'Push-up', 'description': 'A classic upper body exercise', 'instructions': 'Start in a plank position, lower your body to the ground by bending your elbows, then push back up.', 'target_muscles': 'Chest, Shoulders, Triceps'},
        {'name': 'Squats', 'description': 'Great for lower body strength', 'instructions': 'Stand with feet shoulder-width apart, lower your body by bending your knees and hips, keeping your back straight, then return to standing position.', 'target_muscles': 'Quadriceps, Hamstrings, Glutes'},
        {'name': 'Pull-up', 'description': 'An excellent bodyweight exercise for back and arms', 'instructions': 'Hang from a pull-up bar with your hands slightly wider than shoulder-width apart, pull your body up until your chin reaches above the bar, then lower yourself back down with control.', 'target_muscles': 'Back, Biceps'},
        {'name': 'Deadlift', 'description': 'Strengthens the lower back, glutes, and hamstrings', 'instructions': 'Stand with feet shoulder-width apart, bend at the hips and knees to grip the barbell, keeping your back straight, lift the barbell by extending your hips and knees, then lower it back down.', 'target_muscles': 'Lower Back, Glutes, Hamstrings'},
        {'name': 'Bench Press', 'description': 'A popular exercise for building chest strength', 'instructions': 'Lie on a flat bench with your feet planted firmly on the ground, grip the barbell slightly wider than shoulder-width apart, lower the bar to your chest, then press it back up to the starting position.', 'target_muscles': 'Chest, Shoulders, Triceps'},
        {'name': 'Lunges', 'description': 'Effective for building leg strength and balance', 'instructions': 'Stand with feet together, step forward with one foot and lower your body until both knees are bent at a 90-degree angle, then push back up to the starting position and repeat on the other side.', 'target_muscles': 'Quadriceps, Hamstrings, Glutes'},
        {'name': 'Plank', 'description': 'Strengthens the core muscles', 'instructions': 'Start in a push-up position with your arms straight, engage your core and hold your body in a straight line from head to heels, keeping your abs tight and avoiding sagging or arching.', 'target_muscles': 'Abdominals, Obliques, Lower Back'},
        {
    "name": "Chest Flyes","description": "Isolates the chest muscles and helps develop definition", "instructions": "Lie on a flat bench holding dumbbells directly above your chest with palms facing each other, lower the weights out to the sides in a wide arc until your chest feels a stretch, then return to the starting position by squeezing the chest muscles.", "target_muscles": "Chest"
},
{
    "name": "Romanian Deadlift",
    "description": "Focuses on the posterior chain, particularly the hamstrings and glutes",
    "instructions": "Stand with feet hip-width apart, holding a barbell with an overhand grip, hinge at the hips while keeping a slight bend in the knees, lower the bar towards the floor while maintaining a flat back, then return to standing position by squeezing the glutes.",
    "target_muscles": "Hamstrings, Glutes, Lower Back"
},
{
    "name": "Bicep Curls",
    "description": "Targets the biceps and helps build arm strength and size",
    "instructions": "Stand with feet shoulder-width apart, hold a dumbbell in each hand with palms facing forward, curl the weights upwards towards your shoulders while keeping your elbows stationary, then lower the weights back down.",
    "target_muscles": "Biceps"
},

{
    "name": "Barbell Rows",
    "description": "Builds back strength and thickness",
    "instructions": "Stand with feet shoulder-width apart, bend at the hips and knees to grip the barbell with an overhand grip, pull the barbell towards your lower chest while keeping your back straight, then lower it back down.",
    "target_muscles": "Upper Back, Biceps"
},

{
    "name": "Chin-ups",
    "description": "Targets the biceps and upper back",
    "instructions": "Hang from a bar with palms facing towards you, pull your body up until your chin clears the bar, then lower yourself back down with control.",
    "target_muscles": "Biceps, Upper Back"
},

{
    "name": "Hammer Curls",
    "description": "Focuses on the biceps brachii and brachialis",
    "instructions": "Stand with feet shoulder-width apart, hold a dumbbell in each hand with palms facing each other, curl the weights upwards while keeping your palms facing inwards, then lower them back down.",
    "target_muscles": "Biceps, Brachialis"
},

{
    "name": "Inverted Rows",
    "description": "Bodyweight exercise targeting the upper back and biceps",
    "instructions": "Lie under a bar set at about waist height, grab the bar with an overhand grip and hang with arms fully extended, pull your chest towards the bar while keeping your body in a straight line, then lower yourself back down.",
    "target_muscles": "Upper Back, Biceps"
},

{
    "name": "Seated Cable Rows",
    "description": "Isolation exercise for the upper back and biceps",
    "instructions": "Sit at a cable machine with your feet on the footrests, grab the handles with an overhand grip, pull the handles towards your torso while keeping your back straight, then slowly return to the starting position.",
    "target_muscles": "Upper Back, Biceps"
},

{
    "name": "Box Squats",
    "description": "Strengthens the lower body and helps with proper squat form",
    "instructions": "Stand in front of a box or bench, lower your body by bending your knees and hips until you touch the box, then drive through your heels to stand back up.",
    "target_muscles": "Quadriceps, Hamstrings, Glutes"
},

{
    "name": "Romanian Deadlift",
    "description": "Focuses on the posterior chain, particularly the hamstrings and glutes",
    "instructions": "Stand with feet hip-width apart, holding a barbell with an overhand grip, hinge at the hips while keeping a slight bend in the knees, lower the bar towards the floor while maintaining a flat back, then return to standing position by squeezing the glutes.",
    "target_muscles": "Hamstrings, Glutes, Lower Back"
},

{
    "name": "Leg Press",
    "description": "Strengthens the lower body with minimal stress on the lower back",
    "instructions": "Sit on a leg press machine with feet shoulder-width apart, push the platform away by extending your knees, then slowly lower it back down.",
    "target_muscles": "Quadriceps, Hamstrings, Glutes"
},

{
    "name": "Tricep Dips",
    "description": "Targets the triceps and improves upper body strength",
    "instructions": "Sit on the edge of a chair or bench with hands gripping the edge, slide your butt off the edge and lower your body by bending your elbows, then push back up to the starting position.",
    "target_muscles": "Triceps, Shoulders"
},
{
    "name": "Dumbbell Rows",
    "description": "Strengthens the upper back and arms",
    "instructions": "Stand with a dumbbell in each hand, hinge at the hips while keeping your back flat, pull the dumbbells up towards your chest, then lower them back down.",
    "target_muscles": "Upper Back, Biceps"
},
        ]
        for data in exercises_data:
            Exercise.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Exercises successfully added'))



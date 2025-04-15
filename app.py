from flask import Flask, render_template

app = Flask(__name__)

# Exercise data
kettlebell_exercises = [
    "Kettlebell Swing", "Kettlebell Goblet Squat", "Kettlebell Deadlift",
    "Kettlebell Clean", "Kettlebell Snatch", "Kettlebell Press",
    "Kettlebell Push Press", "Kettlebell Turkish Get-Up", "Kettlebell Windmill",
    "Kettlebell High Pull", "Kettlebell Thruster", "Kettlebell Row",
    "Kettlebell Floor Press", "Kettlebell Halo", "Kettlebell Figure Eight",
    "Kettlebell Lunge", "Kettlebell Step-Up", "Kettlebell Russian Twist",
    "Kettlebell Side Bend", "Kettlebell Overhead Squat", "Kettlebell Single-Leg Deadlift",
    "Kettlebell Clean and Press", "Kettlebell Clean and Jerk", "Kettlebell Bottoms-Up Press",
    "Kettlebell Farmer's Walk", "Kettlebell Suitcase Carry", "Kettlebell Rack Carry",
    "Kettlebell Overhead Carry", "Kettlebell Swing to Squat", "Kettlebell Swing to High Pull",
    "Kettlebell Swing to Clean", "Kettlebell Swing to Snatch", "Kettlebell Swing to Press",
    "Kettlebell Swing to Thruster", "Kettlebell Swing to Row", "Kettlebell Swing to Floor Press",
    "Kettlebell Swing to Halo", "Kettlebell Swing to Figure Eight", "Kettlebell Swing to Lunge",
    "Kettlebell Swing to Step-Up"
]

bodyweight_exercises = [
    "Push-Ups", "Squats", "Lunges", "Plank", "Burpees",
    "Mountain Climbers", "Jumping Jacks", "Tricep Dips",
    "Bicycle Crunches", "Leg Raises", "Side Plank",
    "Glute Bridges", "High Knees", "Inchworms", "Superman",
    "Russian Twists", "Wall Sit", "Donkey Kicks",
    "Flutter Kicks", "Bear Crawls"
]

stretch_exercises = [
    "Neck Stretch", "Shoulder Stretch", "Arm Stretch",
    "Chest Stretch", "Back Stretch", "Hip Flexor Stretch",
    "Hamstring Stretch", "Quad Stretch", "Calf Stretch",
    "Ankle Stretch"
]

@app.route('/')
def index():
    return render_template('index.html',
                         kettlebell_exercises=kettlebell_exercises,
                         bodyweight_exercises=bodyweight_exercises,
                         stretch_exercises=stretch_exercises)

if __name__ == '__main__':
    app.run(debug=True)
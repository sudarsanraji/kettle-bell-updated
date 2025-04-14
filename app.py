from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime, timedelta
import time

app = Flask(__name__)

# Exercise data
EXERCISES = {
    "kettlebell": [
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
    ],
    "bodyweight": [
        "Push-Ups", "Squats", "Lunges", "Plank", "Burpees",
        "Mountain Climbers", "Jumping Jacks", "Tricep Dips", "Bicycle Crunches",
        "Leg Raises", "Side Plank", "Glute Bridges", "High Knees", "Inchworms",
        "Superman", "Russian Twists", "Wall Sit", "Donkey Kicks", "Flutter Kicks",
        "Bear Crawls"
    ],
    "stretch": [
        "Neck Stretch", "Shoulder Stretch", "Arm Stretch", "Chest Stretch",
        "Back Stretch", "Hip Flexor Stretch", "Hamstring Stretch", "Quad Stretch",
        "Calf Stretch", "Full Body Stretch"
    ]
}

DAILY_ROUTINES = [
    "Wake Up Early", "Hydrate", "Stretch or Exercise", "Meditate or Practice Mindfulness",
    "Healthy Breakfast", "Plan Your Day", "Personal Hygiene", 
    "Read or Listen to Something Inspirational"
]

@app.route('/')
def index():
    return render_template('index.html', exercises=EXERCISES, routines=DAILY_ROUTINES)

@app.route('/start_workout', methods=['POST'])
def start_workout():
    data = request.json
    exercises = data.get('exercises', [])
    work_time = int(data.get('work_time', 30))
    rest_time = int(data.get('rest_time', 15))
    sets = int(data.get('sets', 3))
    set_rest_time = int(data.get('set_rest_time', 60))
    
    # Simulate workout timing (in a real app, this would be handled client-side)
    workout_data = {
        "total_time": (work_time * len(exercises) * sets) + 
                      (rest_time * (len(exercises) - 1) * sets) + 
                      (set_rest_time * (sets - 1)),
        "exercises": exercises,
        "work_time": work_time,
        "rest_time": rest_time,
        "sets": sets,
        "set_rest_time": set_rest_time
    }
    
    return jsonify(workout_data)

@app.route('/get_sound/<sound_name>')
def get_sound(sound_name):
    # In a real app, you would serve the sound file
    return jsonify({"status": "sound available"})

if __name__ == '__main__':
    app.run(debug=True)
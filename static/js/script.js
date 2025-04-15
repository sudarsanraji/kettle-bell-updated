document.addEventListener('DOMContentLoaded', function() {
    const startWorkoutBtn = document.getElementById('start-workout');
    const pauseWorkoutBtn = document.getElementById('pause-workout');
    const stopWorkoutBtn = document.getElementById('stop-workout');
    const currentExerciseDisplay = document.getElementById('current-exercise');
    const timerDisplay = document.getElementById('timer-display');
    const progressBar = document.getElementById('progress-bar');
    const setInfoDisplay = document.getElementById('set-info');
    const upcomingExercisesList = document.getElementById('upcoming-exercises');
    
    let workoutInterval;
    let currentTime = 0;
    let isPaused = false;
    let currentWorkout = null;
    let isResting = false;
    
    startWorkoutBtn.addEventListener('click', function() {
        const selectedExercises = Array.from(document.querySelectorAll('.exercise-check:checked')).map(el => el.value);
        if (selectedExercises.length === 0) {
            alert('Please select at least one exercise');
            return;
        }
        
        const workTime = parseInt(document.getElementById('work-time').value) || 30;
        const restTime = parseInt(document.getElementById('rest-time').value) || 15;
        const sets = parseInt(document.getElementById('sets').value) || 3;
        const setRestTime = parseInt(document.getElementById('set-rest-time').value) || 60;
        
        currentWorkout = {
            exercises: selectedExercises,
            workTime: workTime,
            restTime: restTime,
            sets: sets,
            setRestTime: setRestTime,
            currentSet: 1,
            currentExerciseIndex: 0
        };
        
        // Update upcoming exercises list
        updateUpcomingExercises();
        
        startSet();
    });
    
    function updateUpcomingExercises() {
        upcomingExercisesList.innerHTML = '';
        const exercisesForSet = [...currentWorkout.exercises];
        
        // Add exercises for current set
        exercisesForSet.forEach((exercise, index) => {
            const li = document.createElement('li');
            li.className = 'list-group-item';
            li.textContent = `${index + 1}. ${exercise}`;
            upcomingExercisesList.appendChild(li);
        });
    }
    
    pauseWorkoutBtn.addEventListener('click', function() {
        if (isPaused) {
            isPaused = false;
            pauseWorkoutBtn.textContent = 'Pause';
            startTimer();
        } else {
            isPaused = true;
            pauseWorkoutBtn.textContent = 'Resume';
            clearInterval(workoutInterval);
        }
    });
    
    stopWorkoutBtn.addEventListener('click', function() {
        clearInterval(workoutInterval);
        currentExerciseDisplay.textContent = "Workout Stopped";
        timerDisplay.textContent = "00:00";
        progressBar.style.width = "0%";
        setInfoDisplay.textContent = "";
        currentWorkout = null;
    });
    
    function startSet() {
        if (currentWorkout.currentSet > currentWorkout.sets) {
            finishWorkout();
            return;
        }
        
        setInfoDisplay.textContent = `Set ${currentWorkout.currentSet} of ${currentWorkout.sets}`;
        currentWorkout.currentExerciseIndex = 0;
        startExercise();
    }
    
    function startExercise() {
        if (currentWorkout.currentExerciseIndex >= currentWorkout.exercises.length) {
            // End of set
            if (currentWorkout.currentSet < currentWorkout.sets) {
                startRestBetweenSets();
            } else {
                finishWorkout();
            }
            return;
        }
        
        const exercise = currentWorkout.exercises[currentWorkout.currentExerciseIndex];
        currentExerciseDisplay.textContent = exercise;
        isResting = false;
        
        startTimer(currentWorkout.workTime, function() {
            // Exercise completed
            currentWorkout.currentExerciseIndex++;
            if (currentWorkout.currentExerciseIndex < currentWorkout.exercises.length) {
                startRest();
            } else {
                // End of set
                if (currentWorkout.currentSet < currentWorkout.sets) {
                    startRestBetweenSets();
                } else {
                    finishWorkout();
                }
            }
        });
    }
    
    function startRest() {
        isResting = true;
        currentExerciseDisplay.textContent = "Rest";
        startTimer(currentWorkout.restTime, function() {
            startExercise();
        });
    }
    
    function startRestBetweenSets() {
        isResting = true;
        currentExerciseDisplay.textContent = "Rest Between Sets";
        startTimer(currentWorkout.setRestTime, function() {
            currentWorkout.currentSet++;
            startSet();
        });
    }
    
    function startTimer(duration, callback) {
        clearInterval(workoutInterval);
        currentTime = duration;
        updateTimerDisplay();
        
        let totalDuration = duration;
        let elapsed = 0;
        
        workoutInterval = setInterval(function() {
            if (!isPaused) {
                currentTime--;
                elapsed++;
                updateTimerDisplay();
                updateProgressBar(elapsed / totalDuration * 100);
                
                if (currentTime <= 0) {
                    clearInterval(workoutInterval);
                    if (callback) callback();
                }
            }
        }, 1000);
    }
    
    function updateTimerDisplay() {
        const minutes = Math.floor(currentTime / 60);
        const seconds = currentTime % 60;
        timerDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    function updateProgressBar(percent) {
        progressBar.style.width = `${percent}%`;
        progressBar.setAttribute('aria-valuenow', percent);
        
        if (isResting) {
            progressBar.classList.remove('bg-primary');
            progressBar.classList.add('bg-success');
        } else {
            progressBar.classList.remove('bg-success');
            progressBar.classList.add('bg-primary');
        }
    }
    
    function finishWorkout() {
        clearInterval(workoutInterval);
        currentExerciseDisplay.textContent = "Workout Complete!";
        timerDisplay.textContent = "00:00";
        progressBar.style.width = "100%";
        setInfoDisplay.textContent = "";
    }
});
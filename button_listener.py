from gpiozero import Button
from subprocess import run
from signal import pause

# Define the GPIO pin for the button
button = Button(17)  # Use the GPIO pin you connected the button to

def execute_script():
    # Execute the checkVisitor.py script
    # venv_path = '/home/ados2405/my_project_env1/bin/activate'
    # exec(open(venv_path).read(), dict(_file_=venv_path))
    venv_python = '/home/ados2405/my_project_env1/bin/python'
    run([venv_python, "Documents/MAIT-Hackathon-main/checkVisitor.py"])  # Update with the actual path

# Attach the execute_script function to the button press
button.when_pressed = execute_script

# Keep the program running
pause()
import subprocess
import os

def execute_task_a1():
    # Install uv if not already installed
    try:
        subprocess.run(["uv", "--version"], check=True, shell=True)
    except subprocess.CalledProcessError:
        subprocess.run(["pip", "install", "uv"], shell=True)

    # Run datagen.py with the user's email as an argument
    user_email = os.getenv("USER_EMAIL")
    subprocess.run(["python", "datagen.py", user_email], shell=True)

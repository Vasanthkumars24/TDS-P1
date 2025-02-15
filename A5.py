import glob
import os

def execute_task_a5():
    # Get all .log files in /data/logs/
    log_files = glob.glob("/data/logs/*.log")

    # Sort files by modification time (most recent first)
    log_files.sort(key=os.path.getmtime, reverse=True)

    # Get the first 10 files
    recent_files = log_files[:10]

    # Extract the first line of each file
    first_lines = []
    for file in recent_files:
        with open(file, "r") as f:
            first_lines.append(f.readline().strip())

    # Write the first lines to a new file
    with open("/data/logs-recent.txt", "w") as file:
        file.write("\n".join(first_lines))

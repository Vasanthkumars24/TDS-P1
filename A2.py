def execute_task_a2():
    # Install prettier if not already installed
    subprocess.run(["npm", "install", "-g", "prettier@3.4.2"], shell=True)

    # Format the file using prettier
    subprocess.run(["npx", "prettier@3.4.2", "--write", "/data/format.md"], shell=True)

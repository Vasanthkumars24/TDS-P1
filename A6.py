import os
import json

def execute_task_a6():
    index = {}
    for root, _, files in os.walk("/data/docs"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    for line in f:
                        if line.startswith("# "):
                            # Extract the title (remove the '# ' prefix)
                            title = line.strip()[2:]
                            # Add to index (relative path as key)
                            relative_path = os.path.relpath(file_path, "/data/docs")
                            index[relative_path] = title
                            break

    # Write the index to a JSON file
    with open("/data/docs/index.json", "w") as file:
        json.dump(index, file, indent=2)

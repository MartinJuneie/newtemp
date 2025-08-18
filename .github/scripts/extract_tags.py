import json
import os

# Load JSON data from file
with open("gar_tags.json", "r") as f:
    data = json.load(f)

# Extract just the tag part (after last slash)
tags = [item["tag"].split("/")[-1] for item in data]

print(tags)

largest_version = None
second_largest_version = None

for item in tags:
    parts = item.split(".")
    if len(parts) == 3 and all(p.isdigit() for p in parts):  # check semantic version
        version_tuple = tuple(map(int, parts))  # convert to integers
        if largest_version is None or version_tuple > largest_version:
            second_largest_version = largest_version  # Update second largest
            largest_version = version_tuple  # Update largest
        elif second_largest_version is None or version_tuple > second_largest_version:
            second_largest_version = version_tuple  # Update second largest

if largest_version:
    largest_version_str = ".".join(map(str, largest_version))
    print("Largest version:", largest_version_str)
else:
    print("No valid versions found")

if second_largest_version:
    second_largest_version_str = ".".join(map(str, second_largest_version))
    print("Second largest version:", second_largest_version_str)
else:
    print("No second largest version found")

output_path = os.getenv("GITHUB_OUTPUT")
if output_path:
    with open(output_path, "a") as f:
        f.write(f"largest_version={largest_version_str}\n")
        f.write(f"second_largest_version={second_largest_version_str}\n")
else:
    print("GITHUB_OUTPUT environment variable not set.")
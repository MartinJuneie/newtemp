import os

val = 88

output_path = os.getenv("GITHUB_OUTPUT")
if output_path:
    with open(output_path, "a") as f:
        f.write(f"value={val}")
else:
    print("GITHUB_OUTPUT environment variable not set.")
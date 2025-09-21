import os

file_path = "grades.txt"

if os.path.exists(file_path):
    try:
        with open(file_path, "r") as f:
            data = f.read()
            print("File contents:\n" + data)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
else:
    print(f"File '{file_path}' does not exist.")
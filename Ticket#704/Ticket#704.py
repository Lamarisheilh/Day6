import logging

logging.basicConfig(level=logging.INFO)

file_path = "grades.txt"

try:
    with open(file_path, "w") as f:
        f.write("Ali, A\n")
        logging.info("Grades successfully written for Ali")

except Exception as e:
    logging.error("Failed to write grades for Ali", e)

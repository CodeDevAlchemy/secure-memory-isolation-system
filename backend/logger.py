import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "security_log.txt")

def log_attack(message):
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")
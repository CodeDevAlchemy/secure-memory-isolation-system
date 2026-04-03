from datetime import datetime

def log_attack(message):
    with open("../logs/security_log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")
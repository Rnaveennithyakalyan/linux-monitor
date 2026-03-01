import psutil
import time
from datetime import datetime
import os

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
LOG_FILE = "system_log.txt"


if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("=== System Resource Monitoring Log ===\n")

def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def monitor_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    processes = len(psutil.pids())

   
    top_processes = sorted(
        psutil.process_iter(['pid', 'name', 'cpu_percent']),
        key=lambda p: p.info['cpu_percent'] if p.info['cpu_percent'] else 0,
        reverse=True
    )[:5]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_message = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Processes: {processes}"
    print(status_message)

    print("Top 5 Processes:")
    for proc in top_processes:
        print(proc.info)

    if cpu > CPU_THRESHOLD or memory > MEM_THRESHOLD:
        alert_message = f"ALERT: High resource usage detected -> {status_message}"
        log_event(alert_message)
        log_event("Top 5 Processes: " + ", ".join([str(proc.info) for proc in top_processes]))

if __name__ == "__main__":
    while True:
        monitor_system()
        time.sleep(5)

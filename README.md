# Linux System Resource Monitoring Tool

A lightweight Python-based monitoring tool for Ubuntu/Linux systems.

## What It Does

- Tracks CPU usage
- Tracks memory usage
- Displays top 5 CPU-consuming processes
- Logs system activity to a file
- Logs alerts when CPU or memory usage exceeds 80%
- Supports safe shutdown using Ctrl + C

## Tech Used

- Python 3
- psutil (for OS-level metrics)

## Run

```bash
python3 monitor.py

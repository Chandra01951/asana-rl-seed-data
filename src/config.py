# src/config.py

# ---------------------------
# ORGANIZATION SCALE
# ---------------------------
USER_COUNT = 6000          # Number of users in the company

# ---------------------------
# DATE RANGES (in days)
# ---------------------------
USER_JOIN_DAYS_RANGE = (30, 900)
TASK_CREATION_DAYS_RANGE = (1, 90)
TASK_COMPLETION_MAX_DAYS = 14

# ---------------------------
# TASK DISTRIBUTIONS
# ---------------------------
TASKS_PER_PROJECT_RANGE = (15, 40)
TASK_UNASSIGNED_RATE = 0.15
TASK_COMPLETION_RATE = 0.65

# ---------------------------
# PROJECT SETTINGS
# ---------------------------
PROJECT_COMPLETED_RATE = 0.65

import random

ENGINEERING_TASKS = [
    "Auth API – Fix token expiration bug",
    "Database – Optimize user query index",
    "Payments – Handle retry logic"
]

MARKETING_TASKS = [
    "Q2 Campaign – Landing page copy",
    "Product Launch – Email sequence",
    "SEO – Blog content update"
]

def generate_task_name(project_type):
    if project_type == "sprint":
        return random.choice(ENGINEERING_TASKS)
    return random.choice(MARKETING_TASKS)

def generate_description():
    options = [
        "",
        "Short task description.",
        "- Step 1\n- Step 2\n- Step 3"
    ]
    return random.choice(options)

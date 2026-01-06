import uuid
from datetime import date, timedelta
import random

ENGINEERING_PROJECTS = [
    "Backend API Revamp",
    "Authentication Service Hardening",
    "Database Performance Optimization"
]

MARKETING_PROJECTS = [
    "Q2 Growth Campaign",
    "Product Launch – Analytics",
    "SEO Content Expansion"
]

OPS_PROJECTS = [
    "Customer Support Workflow Redesign",
    "Billing Process Automation"
]

def generate_projects(team_ids, team_functions):
    projects = []
    today = date.today()

    for team_id, function in zip(team_ids, team_functions):
        if function == "engineering":
            name = random.choice(ENGINEERING_PROJECTS)
            ptype = "sprint"
            max_duration = 30
        elif function == "marketing":
            name = random.choice(MARKETING_PROJECTS)
            ptype = "campaign"
            max_duration = 60
        else:
            name = random.choice(OPS_PROJECTS)
            ptype = "ops"
            max_duration = 90

        start = today - timedelta(days=random.randint(0, 90))

        # 65% completed projects, 35% ongoing
        if random.random() < 0.65:
            duration = random.randint(14, max_duration)
            end = min(start + timedelta(days=duration), today)
        else:
            end = None

        projects.append((
            str(uuid.uuid4()),
            team_id,
            name,
            ptype,
            start,
            end
        ))

    return projects

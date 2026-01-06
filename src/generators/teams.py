import uuid

ENGINEERING_TEAMS = [
    "Backend Platform",
    "Frontend Web",
    "Infrastructure",
    "Data Engineering"
]

MARKETING_TEAMS = [
    "Growth Marketing",
    "Content Marketing",
    "Product Marketing"
]

OPS_TEAMS = [
    "Customer Support",
    "Sales Operations",
    "Finance Operations"
]

def generate_teams(org_id):
    teams = []

    for name in ENGINEERING_TEAMS:
        teams.append((str(uuid.uuid4()), org_id, name, "engineering"))

    for name in MARKETING_TEAMS:
        teams.append((str(uuid.uuid4()), org_id, name, "marketing"))

    for name in OPS_TEAMS:
        teams.append((str(uuid.uuid4()), org_id, name, "ops"))

    return teams

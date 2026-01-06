from models.db import get_connection
from utils.db_utils import execute_many

from generators.organizations import generate_organization
from generators.teams import generate_teams
from generators.users import generate_users
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.comments import generate_comments

from config import USER_COUNT

# --------------------------------
# Database setup
# --------------------------------
conn = get_connection()
cur = conn.cursor()

# Create schema (fresh DB expected)
with open("schema.sql") as f:
    cur.executescript(f.read())

# --------------------------------
# Organization
# --------------------------------
org = generate_organization()
execute_many(conn, "INSERT INTO organizations VALUES (?,?,?,?)", [org])

org_id, _, domain, _ = org

# --------------------------------
# Teams
# --------------------------------
teams = generate_teams(org_id)
execute_many(conn, "INSERT INTO teams VALUES (?,?,?,?)", teams)

team_ids = [t[0] for t in teams]
team_functions = [t[3] for t in teams]

# --------------------------------
# Users
# --------------------------------
users = generate_users(org_id, domain, count=USER_COUNT)
execute_many(conn, "INSERT INTO users VALUES (?,?,?,?,?,?)", users)

user_ids = [u[0] for u in users]

# --------------------------------
# Projects
# --------------------------------
projects = generate_projects(team_ids, team_functions)
execute_many(conn, "INSERT INTO projects VALUES (?,?,?,?,?,?)", projects)

# --------------------------------
# Sections, Tasks, Comments
# --------------------------------
all_comments = []

for project in projects:
    project_id, _, _, project_type, _, _ = project

    # Sections
    sections = generate_sections(project_id)
    execute_many(conn, "INSERT INTO sections VALUES (?,?,?)", sections)
    section_ids = [s[0] for s in sections]

    # Tasks
    tasks = generate_tasks(project_id, section_ids, user_ids, project_type)
    execute_many(conn, "INSERT INTO tasks VALUES (?,?,?,?,?,?,?,?,?,?)", tasks)

    # Comments
    for task in tasks:
        task_id = task[0]
        task_created_at = task[7]  # created_at
        all_comments.extend(
            generate_comments(task_id, user_ids, task_created_at)
        )

# --------------------------------
# Insert all comments
# --------------------------------
if all_comments:
    execute_many(
        conn,
        "INSERT INTO comments VALUES (?,?,?,?,?)",
        all_comments
    )

# --------------------------------
# Finalize
# --------------------------------
conn.commit()
conn.close()

print("Asana simulation database generated successfully.")

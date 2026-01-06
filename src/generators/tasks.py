import uuid
from datetime import datetime, timedelta
import random
from utils.llm_utils import generate_task_name, generate_description
from config import (
    TASK_CREATION_DAYS_RANGE,
    TASK_COMPLETION_RATE,
    TASK_COMPLETION_MAX_DAYS,
    TASK_UNASSIGNED_RATE,
    TASKS_PER_PROJECT_RANGE
)


def generate_tasks(project_id, section_ids, user_ids, project_type):
    tasks = []
    now = datetime.now()

    for _ in range(random.randint(*TASKS_PER_PROJECT_RANGE)):
        # Task creation within last 90 days
        created_at = now - timedelta(
    days=random.randint(*TASK_CREATION_DAYS_RANGE)
)

        # Completion probability (can later vary by project_type)
        completed = random.random() < TASK_COMPLETION_RATE

        completed_at = None
        if completed:
            # Max possible completion window without exceeding now
            max_days = (now - created_at).days
            if max_days > 0:
                completed_at = created_at + timedelta(
                    days=random.randint(1, min(TASK_COMPLETION_MAX_DAYS, max_days))
                )
            else:
                completed_at = created_at

        assignee = (
    random.choice(user_ids)
    if random.random() > TASK_UNASSIGNED_RATE
    else None
)


        tasks.append((
            str(uuid.uuid4()),
            project_id,
            random.choice(section_ids),
            assignee,
            generate_task_name(project_type),
            generate_description(),
            None,               # due_date
            created_at,
            completed,
            completed_at
        ))

    return tasks

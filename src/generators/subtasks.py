import uuid
import random

SUBTASK_TEMPLATES = [
    "Design approach",
    "Implement logic",
    "Write tests",
    "Review changes"
]

def generate_subtasks(task_id):
    subtasks = []

    for name in random.sample(SUBTASK_TEMPLATES, random.randint(1, 3)):
        subtasks.append((
            str(uuid.uuid4()),
            task_id,
            name,
            random.random() < 0.6
        ))

    return subtasks

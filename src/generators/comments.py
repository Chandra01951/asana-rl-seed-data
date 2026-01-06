import uuid
from datetime import datetime, timedelta
import random

COMMENTS = [
    "Please review this today.",
    "I have pushed the fix.",
    "This is ready for QA.",
    "Marked this as done.",
    "Adding this for visibility.",
    "Looping in the relevant stakeholders.",
    "Blocked due to dependency.",
    "Waiting on API changes from another team.",
    "This is blocked until the design is finalized.",
    "Dependency not resolved yet.",
    "On hold pending approval.",
    "Can you clarify the expected behavior here?",
    "Is this still a priority?",
    "Any update on this?",
    "Left comments on the PR.",
    "Looks good to me.",
    "Approved from my side.",
    "We can target this for the next sprint.",
    "Resolved and closing this."
]

def generate_comments(task_id, user_ids, task_created_at):
    comments = []
    now = datetime.now()

    for _ in range(random.randint(0, 3)):
        created_at = min(
            task_created_at + timedelta(hours=random.randint(1, 72)),
            now
        )

        comments.append((
            str(uuid.uuid4()),
            task_id,
            random.choice(user_ids),
            random.choice(COMMENTS),
            created_at
        ))

    return comments

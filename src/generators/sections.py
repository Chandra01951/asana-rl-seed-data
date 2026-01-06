import uuid

def generate_sections(project_id):
    return [
        (str(uuid.uuid4()), project_id, "To Do"),
        (str(uuid.uuid4()), project_id, "In Progress"),
        (str(uuid.uuid4()), project_id, "Done"),
    ]

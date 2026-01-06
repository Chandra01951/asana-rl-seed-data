import uuid

def generate_custom_fields(project_id):
    return [
        (str(uuid.uuid4()), project_id, "Priority", "enum"),
        (str(uuid.uuid4()), project_id, "Effort", "number")
    ]

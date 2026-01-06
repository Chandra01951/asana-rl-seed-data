import uuid

TAG_NAMES = [
    "bug", "urgent", "backend", "frontend",
    "performance", "security", "documentation"
]

def generate_tags():
    return [(str(uuid.uuid4()), tag) for tag in TAG_NAMES]

import uuid
from faker import Faker
from datetime import datetime, timedelta
from config import USER_JOIN_DAYS_RANGE
import random

fake = Faker()

# Role hierarchy inspired by real SaaS org structures
ROLES = [
    "IC",
    "Senior IC",
    "Lead",
    "Manager",
    "Senior Manager",
    "Director"
]

# Approximate enterprise distribution (bottom-heavy org)
ROLE_WEIGHTS = [45, 20, 15, 10, 7, 3]

def generate_users(org_id, domain, count):
    """
    Generates synthetic users for a single organization.
    - Ensures unique emails (required by DB constraint)
    - Distributes roles realistically
    - Spreads join dates over the last ~3 years
    """
    users = []
    seen_emails = set()

    for _ in range(count):
        uid = str(uuid.uuid4())
        name = fake.name()

        # Email derived from name; uniqueness enforced via UUID suffix if needed
        base_email = name.replace(" ", ".").lower()
        email = f"{base_email}@{domain}"
        if email in seen_emails:
            email = f"{base_email}.{uid[:6]}@{domain}"
        seen_emails.add(email)

        # Weighted random role assignment
        role = random.choices(ROLES, weights=ROLE_WEIGHTS, k=1)[0]

        # Join date spread to simulate gradual hiring growth
        joined_at = datetime.now() - timedelta(
    days=random.randint(*USER_JOIN_DAYS_RANGE)
)



        users.append((uid, org_id, name, email, role, joined_at))

    return users

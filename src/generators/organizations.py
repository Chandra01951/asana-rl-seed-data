import uuid
from datetime import datetime
from scrapers.company_names import get_company_name

def generate_organization():
    company_name = get_company_name()
    domain = company_name.lower() + ".com"

    return (
        str(uuid.uuid4()),   # org_id
        company_name,        # name
        domain,              # domain
        datetime.now()       # created_at
    )

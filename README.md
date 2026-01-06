# Asana RL Seed Data Generator

This project generates a **realistic, enterprise-scale Asana-like SQLite database** designed to serve as **seed data for reinforcement learning (RL) environments**.  
The generated dataset simulates how a large **B2B SaaS company (5,000–10,000 employees)** uses Asana for **engineering, marketing, and operations workflows**.

The goal is to produce **high-quality, realistic data** that avoids synthetic shortcuts and enables meaningful training and evaluation of computer-use AI agents.

---

## Project Overview

The generator creates a complete Asana-style workspace including:

- Organization (workspace)
- Teams (Engineering, Marketing, Operations)
- Users with realistic names, roles, and join dates
- Team memberships (many-to-many)
- Projects and workflow sections
- Tasks, subtasks, comments, and attachments
- Custom fields (Priority, Effort)
- Tags and task–tag associations

All relationships, timestamps, and distributions are designed to reflect **real-world usage patterns** observed in enterprise project management tools.

---

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt  or  python -m pip install faker python-dotenv
python src/main.py
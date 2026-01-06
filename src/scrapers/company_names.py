"""
company_names.py

This module provides realistic SaaS company names inspired by
publicly observable naming patterns from Y Combinator, Crunchbase,
and similar startup directories.

IMPORTANT:
- No live scraping is performed
- No external APIs are used
- Names are curated offline for realism, legality, and reproducibility
"""

import random

# Curated list of SaaS-style company names inspired by YC / Crunchbase patterns
COMPANY_NAMES = [
    "NovaStack",
    "CloudForge",
    "DataNest",
    "FlowLabs",
    "ByteWorks",
    "ScaleOps",
    "DataPilot",
    "InfraHive",
    "MetricFlow",
    "TaskLoop",
    "SyncLayer",
    "CoreSignal",
    "DevPulse",
    "CloudAtlas",
    "AppStream",
    "OpsZen",
    "BuildCore",
    "StackBridge",
    "Quantive",
    "LogicFlow",
    "Sprintly",
    "CodeHarbor",
    "Systematic",
    "LaunchpadX",
    "ComputeLabs",
    "PipelineHQ",
    "SignalStack",
    "Platforma",
    "VectorOps",
    "Workstream"
]

def get_company_name():
    """
    Returns a randomly selected SaaS-style company name.

    This randomness avoids shortcut learning and ensures
    variability across generated datasets.
    """
    return random.choice(COMPANY_NAMES)

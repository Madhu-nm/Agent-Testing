# src/agent/nodes/fetch_prs.py
from services.github_service import get_merged_prs

def run(state):
    state.prs = get_merged_prs()
    return state

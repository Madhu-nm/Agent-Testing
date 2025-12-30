# src/agent/nodes/generate_notes.py
from services.openai_service import generate_release_notes

def run(state):
    state.release_notes = generate_release_notes(
        state.prs, state.jira_ids
    )
    return state

# src/agent/state.py
from pydantic import BaseModel
from typing import List, Dict

class AgentState(BaseModel):
    prs: List[Dict] = []
    jira_ids: List[str] = []
    release_notes: str = ""

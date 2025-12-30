
from services.jira_parser import extract_jira_ids

def run(state):
    jira_ids = set()
    for pr in state.prs:
        jira_ids.update(extract_jira_ids(pr["title"]))

    state.jira_ids = sorted(jira_ids)
    return state

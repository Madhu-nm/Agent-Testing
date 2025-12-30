# src/services/jira_parser.py
import re

JIRA_PATTERN = re.compile(r"\b[A-Z]{2,10}-\d+\b")

def extract_jira_ids(text: str) -> list[str]:
    return JIRA_PATTERN.findall(text)

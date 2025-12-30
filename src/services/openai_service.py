# src/services/openai_service.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_release_notes(prs, jira_ids):
    prompt = f"""
You are a senior release manager.

Create clean release notes from the following PRs.

PRs:
{prs}

Jira IDs:
{jira_ids}

Rules:
- Group by Features / Fixes / Improvements
- Use bullet points
- Professional tone
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )
    return response.choices[0].message.content

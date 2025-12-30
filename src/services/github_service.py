import os
from datetime import timezone
from github import Github
from services.release_tracker import get_last_release_time


def get_merged_prs(base_branch: str = "dev") -> list[dict]:
    """
    Fetch merged PRs from the given base branch,
    filtered by merge date to avoid duplicates.
    """

    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")

    if not token or not repo_name:
        raise RuntimeError("GITHUB_TOKEN or GITHUB_REPOSITORY not set")

    github = Github(token)
    repo = github.get_repo(repo_name)

    last_release_time = get_last_release_time()

    pulls = repo.get_pulls(
        state="closed",
        base=base_branch,
        sort="updated",
        direction="asc",
    )

    merged_prs = []

    for pr in pulls:
        if not pr.merged:
            continue

        merged_at = pr.merged_at.replace(tzinfo=timezone.utc)

        # 🚫 Skip already released PRs
        if merged_at <= last_release_time:
            continue

        merged_prs.append({
            "number": pr.number,
            "title": pr.title,
            "author": pr.user.login,
            "merged_at": merged_at.isoformat(),
            "url": pr.html_url,
        })

    return merged_prs

from datetime import datetime, timezone
from pathlib import Path

LAST_RELEASE_FILE = ".last_release"


def get_last_release_time() -> datetime:
    """
    Returns the last release timestamp.
    If file does not exist, return minimum datetime.
    """
    if not Path(LAST_RELEASE_FILE).exists():
        return datetime.min.replace(tzinfo=timezone.utc)

    value = Path(LAST_RELEASE_FILE).read_text().strip()
    return datetime.fromisoformat(value)


def update_last_release_time(dt: datetime) -> None:
    """
    Persist the latest release timestamp.
    """
    Path(LAST_RELEASE_FILE).write_text(dt.isoformat())

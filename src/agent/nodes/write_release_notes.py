from pathlib import Path
from datetime import datetime, timezone
from services.release_tracker import update_last_release_time


def run(state):
    Path("release-notes.md").write_text(state.release_notes)

    # Update release timestamp AFTER successful generation
    update_last_release_time(datetime.now(timezone.utc))

    return state

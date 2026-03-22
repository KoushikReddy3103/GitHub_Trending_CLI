from datetime import datetime, timedelta, timezone

DURATION_MAP = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365,
}

def get_start_date(duration: str) -> str:
    """
    Returns ISO formatted date string based on duration.
    """
    if duration not in DURATION_MAP:
        raise ValueError(f"Invalid duration: {duration}")
    
    days = DURATION_MAP[duration]
    start_date = datetime.now(timezone.utc) - timedelta(days=days)
    return start_date.strftime("%Y-%m-%d")

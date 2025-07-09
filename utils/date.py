from datetime import datetime, timedelta, timezone


def get_yesterdays_date():
    today = datetime.now(timezone.utc)  # use UTC for consistency with most APIs
    yesterday = today - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')  # format as YYYY-MM-DD
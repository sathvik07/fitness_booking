from datetime import datetime
from pytz import timezone, UnknownTimeZoneError

# Default timezone for classes (IST)
IST = timezone("Asia/Kolkata")

def convert_ist_to_timezone(dt: datetime, target_tz: str) -> datetime:
    try:
        target_timezone = timezone(target_tz)
    except UnknownTimeZoneError:
        target_timezone = IST  # fallback to IST if invalid

    ist_aware = IST.localize(dt)
    return ist_aware.astimezone(target_timezone)

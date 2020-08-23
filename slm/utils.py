from datetime import datetime

def str_to_datetime(s: str) -> datetime:
    """Convert a string with the format YYYYMMDD hhmmss to a datetime
    """
    s1, s2 = s.split()
    year, month, day = int(s1[:4]), int(s1[4:6]), int(s1[6:8])
    hour, minute, second = int(s2[:2]), int(s2[2:4]), int(s2[4:6])
    return datetime(year, month, day, hour, minute, second)
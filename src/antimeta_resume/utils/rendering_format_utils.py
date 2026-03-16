from datetime import datetime
from typing import Any

def format_date(value: Any) -> str:
    if not value:
        return "Present"

    text = str(value).strip().replace("Z", "+00:00")
    try:
        if len(text) == 7:
            return datetime.strptime(text, "%Y-%m").strftime("%b %Y")
        if len(text) == 10:
            return datetime.strptime(text, "%Y-%m-%d").strftime("%b %Y")
        return datetime.fromisoformat(text).strftime("%b %Y")
    except ValueError:
        return "Present"

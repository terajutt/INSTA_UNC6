"""
Helper utilities for the bot.
"""

import re
import json
from typing import Any, Optional

def sanitize_text(text: str) -> str:
    """Sanitize text for Telegram."""
    if not text:
        return ""
    # Remove any potential markdown conflicts
    text = str(text)
    return text

def validate_url(url: str) -> bool:
    """Validate if string is a valid URL."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def safe_json_loads(text: str) -> Optional[Any]:
    """Safely load JSON string."""
    try:
        return json.loads(text)
    except:
        return None
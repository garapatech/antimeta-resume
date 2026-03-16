from typing import Any
from urllib.parse import urlparse
from markupsafe import Markup
from markupsafe import escape

def wrap_mail(address: Any) -> Markup:
    if not address:
        return Markup("")

    text = escape(str(address).strip())
    return Markup(f'<a href="mailto:{text}">{text}</a>')

def wrap_url(url: Any) -> Markup:
    if not url:
        return Markup("")

    text = str(url).strip()
    label = text.split("://", 1)[1] if urlparse(text).scheme else text
    return Markup(f'<a href="{escape(text)}">{escape(label)}</a>')

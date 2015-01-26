"""
replies to ping
"""
import re


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"ping", text)
    if not match:
        return

    return u'pong'

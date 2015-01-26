"""
puts dragon picture!
"""
import re


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"(dragon)|(zmaj)", text)
    if not match:
        return

    image_url = u'http://i.imgur.com/jmNZZ7s.jpg'

    return u'warning: {}'.format(image_url)

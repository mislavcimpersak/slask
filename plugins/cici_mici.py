"""
puts cici mici picture!
"""
import re


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"cici mici", text)
    if not match:
        return

    image_url = u'http://i.ytimg.com/vi/Gn3jF8QIZDI/hqdefault.jpg'

    return u'{}'.format(image_url)

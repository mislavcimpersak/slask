"""
puts spam picture!
"""
import random
import re


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"(spam)|(spem)", text)
    if not match:
        return

    img_list = [
        u'https://nononprofitspam.files.wordpress.com/2011/03/markasspam.jpg',
        u'http://www.geekalerts.com/u/SPAM-Hat.jpg',
        u'http://www.ilikeweirdstuff.com/wp-content/uploads/2013/02/SPAM-Lip-Glaze-Balm_13508-l.jpg',
        u'http://images.bwbx.io/cms/2012-05-16/etc_opener21__01__630x420.jpg',
        ]
    image_url = random.choice(img_list)

    return u'{}'.format(image_url)

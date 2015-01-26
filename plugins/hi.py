# -*- coding: utf-8 -*-
"""
hi
"""
import re


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"(\\o)|(o/)", text)
    if not match:
        return

    return u'{}'.format(u'o/')

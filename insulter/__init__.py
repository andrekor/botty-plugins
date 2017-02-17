
import asyncio, aiohttp, re, os
import plugins
import logging
import random
import io

logger = logging.getLogger(__name__)

def _initialise(bot):
    plugins.register_user_command(["insult"])

def insult(bot, event, *args):
    if event.user.is_self:
        return

    if len(args) == 0:
        yield from bot.coro_send_message(event.conv_id, "I duno who to insult")
        return

    url = 'http://autoinsult.datahamster.com/scripts/webinsult.server.php?xajax=generate_insult&xajaxargs[]=3'
    r = yield from aiohttp.request("get", url)
    xml = yield from r.text()
    text = re.search(r"\!\[CDATA\[You(.*?)\]\]", xml).group(1)
    yield from bot.coro_send_message(event.conv_id, " ".join(args) + ' is a' + text)

import asyncio
import time
import schedule

import Messages as msg

class Timer:
    stop_timer = False
    time = 0
    message = ""
    bot = ""

    def __init__(self ,bot, message, time):
        self.time = time
        self.message = message
        self.bot = bot

    async def start(self):
        message_deleted = False
        for i in range(self.time * 10):
            await asyncio.sleep(6)
            if self.stop_timer:
                message_deleted = True
                break
        if not message_deleted:
            await msg.delete_message(self.bot, self.message)

    def stop(self):
        self.stop_timer = True
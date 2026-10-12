import asyncio
import json
import random

from channels.generic.websocket import AsyncWebsocketConsumer


class NumberGenerator(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.number_task = asyncio.create_task(self.send_numbers())

    async def disconnect(self, code):
        self.number_task.cancel()
        try:
            await self.number_task
        except asyncio.CancelledError:
            pass

    async def send_numbers(self):
        while True:
            data = {
                'number': random.randint(1, 1000)
            }

            await self.send(text_data=json.dumps(data))
            await asyncio.sleep(1)
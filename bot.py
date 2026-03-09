import discord
from dotenv import dotenv_values
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

config = dotenv_values(".env")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('Hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config['Token_Code'])





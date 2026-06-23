# Made by tomas
# Its a discord bot where it reads messages and an uncensored AI replies.


# Load env file
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# ollama
import ollama

# Discord bot
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/matan"):
        # Reads the message then give it to an ai
        result = ollama.generate(model=os.getevn("OLLAMA_MODEL"), prompt=message.content)
        await message.channel.send(result['response'])

client.run(os.getenv('DISCORD_TOKEN'))




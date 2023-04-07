import os
import discord

from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=..., intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1058630695762808944



client = discord.Client()

@tasks.loop(hours=24)
async def test(channel,day):
    day += 1
    if (day < 31):
        await channel.send(f"Happy Birthday Sela Day {day}!")

@client.event
async def on_ready():
    day = 6

    channel = client.get_channel(CHANNEL_ID)
    test.start(channel=channel, day=day)

client.run(TOKEN)
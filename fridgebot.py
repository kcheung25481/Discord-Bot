import os
import discord
import datetime
from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()

bot = commands.Bot(command_prefix=..., intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')

# Plane Server
CHANNEL_ID = 1058630695762808944

# Sela's ID
TARGET_USER_ID = 231139951692087306  

# Nio's ID
TARGET_USER_ID1 = 148338773887811587

# Nio's ID
TARGET_USER_ID2 = 759028693229895700

# # Testing
# # My Server
# CHANNEL_ID = 916413818429636693
# # My ID
# TARGET_USER_ID = 140288321002668032

client = discord.Client()

@tasks.loop(hours=24)
async def test(channel):
    day = datetime.datetime.now().day

    await channel.send(f"Happy Birthday Sela Day {day}!")
    await channel.send(f"Happy Birthday Nio Day {day-7}!")
    await channel.send(f"Happy Birthday Pota Day {day-13}!")

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    test.start(channel=channel)

@client.event
async def on_message(message):
    # Check if the message author is the target user
    if message.author.id == TARGET_USER_ID or message.author.id == TARGET_USER_ID1 or message.author.id == TARGET_USER_ID2:
        # Add the desired reactions to the message
        await message.add_reaction('🇭')
        await message.add_reaction('🇦')
        await message.add_reaction('🇵')
        await message.add_reaction('🇸')
        await message.add_reaction('🎂')     

client.run(TOKEN)
import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# Flask server (عشان Render ما يطفّي البوت)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = os.environ.get("TOKEN")  # نخلي التوكن في Environment Variable
GUILD_ID = 123456789012345678
VOICE_CHANNEL_ID = 123456789012345678

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(VOICE_CHANNEL_ID)

    try:
        await channel.connect()
        await guild.change_voice_state(channel=channel, self_mute=True, self_deaf=True)
        print("دخل الروم وهو ميوت ودفن")
    except Exception as e:
        print(e)

keep_alive()
bot.run(TOKEN)
import discord
from discord.ext import commands
from g4f.client import Client
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="?")
client = Client()
@bot.command()
async def ipgeo
@bot.command()
async def gpt(ctx, *, prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    gpt_response = str(response.choices[0].message.content)
    await ctx.send(str(gpt_response))
bot.run(token)
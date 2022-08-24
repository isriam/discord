# bot.py
import os

import discord

TOKEN = 'MTAxMjEwMTk1NDgzMjQ0NTU2MA.G6XQ5b.mCEcH8FuDBewRg_PWZQ5oFAO7Kdk9SbVIMI698'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

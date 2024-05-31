# We The Hobby Discord Bot
# Alex Tedesco

# Imports:
import discord
from discord.ext import commands
import os

cogs = ['modules.socials', 'modules.sms','modules.miscellaneous']

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

# Removes the default help command
client.remove_command('help')

@client.event
async def on_ready():
    # Loads cogs collections
    for cog in cogs:
        await client.load_extension(cog)
    # Logs bot into Discord
    await client.tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="all of you!"))
    print("We have logged in as {0.user}".format(client))

# Runs the Bot
client.run(os.getenv("wth_discord_token")) # Add an environment variable to local system
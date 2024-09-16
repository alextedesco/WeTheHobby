import discord
from discord.ext import commands
import random
import json

words_to_check = ["can", "someone", "door"]

with open('configs.json', 'r') as f:
    json_configs = json.load(f)

class door (commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    # Listens to messages sent in server
    async def on_message (self, message: discord.Message):
        channel = self.client.get_channel(836269101403602954)
        if message.channel.id == 836269101403602954 and message.author.id != 1242223694693007472:
                msg = str(message.content).lower()  
                if (all([x in msg for x in words_to_check])):
                    # Select a random door message response  
                    door_key, door_msg = random.choice(list(json_configs["door-message-responses"].items()))  
                    
                    # Check if the door message has an "image" key and send the appropriate message  
                    if "image" in door_msg and door_msg["image"]:  
                        await channel.send(door_msg["message"], file=discord.File(door_msg["image"]))  
                    else:  
                        await channel.send(door_msg["message"])
            
async def setup (client):
    await client.add_cog(door(client))
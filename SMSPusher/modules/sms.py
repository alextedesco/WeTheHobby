import discord
from discord.ext import commands
import os
import json
from twilio.rest import Client
from modules.miscellaneous import perms_check
from typing import Literal

account_sid = os.environ['TWILIO_ACCOUNT_SID'] # Add an environment variable to local system
auth_token = os.environ['TWILIO_AUTH_TOKEN'] # Add an environment variable to local system
sms_client = Client(account_sid, auth_token)

with open('configs.json', 'r') as f:
    json_configs = json.load(f)

class sms (commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    # Listens to messages sent in server
    async def on_message (self, message: discord.Message):
        current_channel_id = str(message.channel.id)
    
        for user_id in json_configs["discord-ids"]:
            channels = json_configs["discord-ids"][user_id]["channels"]
            phone_number = json_configs["discord-ids"][user_id]["number"]
            for channel in channels.values():
                channel_id = str(channel["id"])
                if channel_id == current_channel_id:
                    # Kinda DRY code block. Solve in future commit ??
                    if str(channel["type"]) == "all":
                        if message.attachments:
                            attachment = message.attachments[0].url
                            send_sms(phone_number, message.clean_content, attachment)
                        else:
                            send_sms (phone_number, message.clean_content)
                    if str(channel["type"]) == "mentions":
                        for user_mention in message.mentions:
                            if str(user_mention.id) ==  str(user_id):
                                if message.attachments:
                                    attachment = message.attachments[0].url 
                                    send_sms(phone_number, message.clean_content, attachment)
                                else:
                                    send_sms(phone_number, message.clean_content)

    @commands.hybrid_command(name="subscribe", with_app_command=True, description="Used by TSE Dev team to add text-channels to database for tech-support alerts", aliases=["alert"])
    
    async def subscribe(self, ctx, channel: discord.TextChannel = None, *, alert_type: Literal['all', 'mentions']): 
        perms = perms_check (ctx)
        if perms:
            if str (ctx.author.id) not in json_configs["discord-ids"].keys():
                await ctx.send ("UserID not in database; subscribe rejected!")
            else:
                if str(channel.id) not in json_configs["discord-ids"][str(ctx.author.id)]["channels"].values():
                    new_channel = {
                        "id": str (channel.id),
                        "type": str (alert_type)
                    }
                    json_configs["discord-ids"][str (ctx.author.id)]["channels"][str(channel.name)] = new_channel
                    with open('configs.json', 'w') as f:
                        json.dump (json_configs, f, indent=3, sort_keys=False)
                else:
                    json_configs["discord-ids"][str (ctx.author.id)]["channels"][str(channel.name)]["type"] = str (alert_type)
                await ctx.send (ctx.author.nick + " has been subscribed to " + str(channel.name))
        else:
            await ctx.send (ctx.author.nick + " does not have perms to add SMS push alerts")

def send_sms (phone_number, message, attachment=None):
    '''
    Uses the Twilio API to send the SMS message
    '''
    ellipsis = "..." if len(message) > 153 else ""

    sms_params = {
        'body': message[:150] + ellipsis,
        'from_': '+15855656027',
        'to': phone_number
    }

    if attachment:
        sms_params['media_url'] = [attachment]

    message = sms_client.messages.create(**sms_params)
    print(message.sid)
   
async def setup (client):
    await client.add_cog(sms(client))
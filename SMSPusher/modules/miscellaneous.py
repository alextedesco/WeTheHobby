import discord
import json
from discord.ext import commands

with open ("configs.json") as f:
    json_configs = json.load(f)

class miscellaneous (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["employeecount"])
    async def membercount(self, ctx):
        '''
        Displays how many members are in the server - [prefix]membercount 
        '''
        embedVar = discord.Embed(title="Top Shelf Enterprises - Employee Count", color=0xA923CF)
        embedVar.add_field(name="Member Count", value=ctx.guild.member_count, inline=False)
        await ctx.send(embed=embedVar)

    @commands.command(aliases=["latency"])
    async def ping(self, ctx):
        '''
        Outputs the latency of the bot
        '''
        await ctx.send(f'Ping is {round(self.client.latency * 1000)} ms')

    @commands.command()
    async def say(self, ctx, channel: discord.TextChannel = None, *, message):
        '''
        Sends messages in specific channels - [prefix]say #[channel] [message]
        '''
        perms = perms_check (ctx)
        if perms:
            await channel.send(message)

    @commands.command()
    async def shutdown(self, ctx):
        '''
        Emergency command that turns off the bot and can only be used by members with Dev Role - [prefix]shutdown
        '''
        perms = perms_check (ctx)
        if perms:
            await ctx.send("Goodbye :(")
            await self.client.close()

    @commands.hybrid_command(name="help", with_app_command=True, description="Output help command with information about bot commands")
    async def help(self, ctx):
        '''
        Help command
        '''
        embedVar = discord.Embed(title="WeTheHobby Commands", color=0x22B14C)
        embedVar.add_field(name="**Social Medias:**", value= "facebook - Outputs WeTheHobby Facebook - [prefix]facebook  \n fanaticslive - Outputs WeTheHobby Fanatics Live - [prefix]fanaticslive \n  instagram - Outputs WeTheHobby Instagram - [prefix]instagram \n socials - Outputs WeTheHobby Socials - [prefix]socials \n tiktok - Outputs WeTheHobby TikTok - [prefix]tiktok \n twitter - onlyfans — Outputs WeTheHobby Twitter - [prefix]twitter \n website — Outputs WeTheHobby Website - [prefix]website \n whatnot — Outputs WeTheHobby Whatnot - [prefix]whatnot \n youtube — Outputs WeTheHobby YouTube - [prefix]youtube", inline=False)
        
        embedVar.add_field(name="**SMS:**", value= 'subscribe — Adds text channel to the SMS database for that user. Only can be used by Devs - [prefix]subscribe [#text-channel] [alert_type ("all" or "mentions")]', inline=False)
        
        embedVar.add_field(name="**Miscellaneous Commands:**", value="membercount — Displays how many members (employees) are in the server - [prefix]membercount \n ping — Outputs the latency of the bot - [prefix]ping \n say — Sends messages in specific channels. Only can be used by Devs - [prefix]say [#text-channel] [message] \n shutdown — Emergency command that turns off the bot. Only can be used by Devs - [prefix]shutdown", inline=False)
        await ctx.send(embed=embedVar, ephemeral=True)

def perms_check (ctx):
    '''
    Helper function to check if user has dev permissions to run a command
    '''
    for json_role in json_configs["discord-roles"].values():
        role_id = int(json_role)

    if discord.utils.get(ctx.author.roles, id=role_id):
        return True

async def setup (client):
    await client.add_cog(miscellaneous(client))
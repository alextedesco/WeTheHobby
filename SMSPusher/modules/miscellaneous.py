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

    @commands.hybrid_command(name="poll", with_app_command=True, description="Creates a poll in a specific channel - [prefix]poll #[channel] [input_text]")

    async def poll(self, ctx, channel: discord.TextChannel = None, *, input_text: str):
        '''
        Creates a poll in a specific channel - [prefix]poll #[channel] Title, option1, option2, ...
        '''
        perms = perms_check(ctx)
        if not perms:
            await ctx.send("You do not have permission to use this command.")
            return

        if not channel:
            await ctx.send("Please specify a channel to send the poll.")
            return

        # Split the input text by commas
        parts = [part.strip() for part in input_text.split(",")]

        if len(parts) < 2:
            await ctx.send("A poll must have at least a title and one option.")
            return

        title = parts[0]
        options = parts[1:]

        if len(options) > 10:
            await ctx.send("A poll can have at most 10 options.")
            return
        
        emoji_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        description = "\n".join(f"{emoji_numbers[i]} {option}" for i, option in enumerate(options))
        embed = discord.Embed(title=title, description=description, color=0x22B14C)
        await ctx.send("Poll created!", ephemeral=True)
        poll_message = await channel.send(embed=embed)

        # Add reactions for voting
        for i in range(len(options)):
            await poll_message.add_reaction(emoji_numbers[i])

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
        embedVar.add_field(name="**Social Medias:**", value= "facebook - Outputs WeTheHobby Facebook - [prefix]facebook  \n fanaticslive - Outputs WeTheHobby Fanatics Live - [prefix]fanaticslive \n  instagram - Outputs WeTheHobby Instagram - [prefix]instagram \n socials - Outputs WeTheHobby Socials - [prefix]socials \n tiktok - Outputs WeTheHobby TikTok - [prefix]tiktok \n twitter — Outputs WeTheHobby Twitter - [prefix]twitter \n website — Outputs WeTheHobby Website - [prefix]website \n whatnot — Outputs WeTheHobby Whatnot - [prefix]whatnot \n youtube — Outputs WeTheHobby YouTube - [prefix]youtube", inline=False)
        
        embedVar.add_field(name="**SMS:**", value= 'subscribe — Adds text channel to the SMS database for that user. Only can be used by Devs - [prefix]subscribe [#text-channel] [alert_type ("all" or "mentions")]', inline=False)
        
        embedVar.add_field(name="**Miscellaneous Commands:**", value="membercount — Displays how many members (employees) are in the server - [prefix]membercount \n ping — Outputs the latency of the bot - [prefix]ping \n say — Sends messages in specific channels. Only can be used by Devs - [prefix]say [#text-channel] [message] \n shutdown — Emergency command that turns off the bot. Only can be used by Devs - [prefix]shutdown", inline=False)
        await ctx.send(embed=embedVar, ephemeral=True)


    @commands.hybrid_command(name="help_role", with_app_command=True, description="Used by TSE IT team to add and remove the help role for tech support")
    async def help_role (self, ctx):
        perms = perms_check (ctx)
        nickname = get_name(ctx)
        logging_channel = ctx.guild.get_channel(int(json_configs["discord-channels"]["help-role-channel-logging"]))

        if perms:
            help_role = ctx.guild.get_role(int(json_configs["discord-roles"]["help"])) 
            action_message = ""
            if help_role in ctx.author.roles:
                # If user already has the role, remove it
                await ctx.author.remove_roles(help_role)
                action_message = f"{nickname} has **removed** the help role!"
            else:
                # If user doesn't have the role, add it
                await ctx.author.add_roles(help_role)
                action_message = f"{nickname} has **added** the help role!"
            await ctx.send(action_message, ephemeral=True)
            await logging_channel.send(action_message)            
        else:
            await ctx.send("You do not have perms to use this command!", ephemeral=True)

    @commands.hybrid_command(name="help role status", with_app_command=True, description="Output status of help role members")
    async def help_role_status(ctx):
        help_role = ctx.guild.get_role(int(json_configs["discord-roles"]["help"]))
        it_role = ctx.guild.get_role(int(json_configs["discord-roles"]["it"]))
        dev_role = ctx.guild.get_role(int(json_configs["discord-roles"]["dev"]))

        embedVar = discord.Embed(title="Help Role Members", color=0x22B14C)
        member_status = ""

        dev_it_members = set(it_role.members + dev_role.members)

        for member in dev_it_members:
            if help_role in member.roles:
                status = "Yes"
            else:
                status = "No"

            member_status += member.display_name + " — " + status + "\n"

        embedVar.add_field(
            name="**Dev/IT Users**",
            value=member_status,
            inline=False
        )

        await ctx.send(embed=embedVar)

    @commands.command(aliases=["presence", "changestatus"])
    async def status(self, ctx, status):
        '''
        Changes the status of the bot and can only be used by members with Dev Role - [prefix]status
        '''
        perms = perms_check (ctx)
        if perms:
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="custom", state=status))

def perms_check (ctx):
    '''
    Helper function to check if user has dev permissions to run a command
    '''
    for json_role in json_configs["discord-roles"].values():
        role_id = int(json_role)

        if discord.utils.get(ctx.author.roles, id=role_id):
            return True

    return False

def get_name(user):
    # if ctx or message
    if hasattr(user, "author"):
        user = user.author

    if user.nick:
        return user.nick
    elif user.display_name:
        return user.display_name
    else:
        return user.name

async def setup (client):
    await client.add_cog(miscellaneous(client))
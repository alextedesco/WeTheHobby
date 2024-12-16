import discord
from discord.ext import commands

class socials (commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="instagram", with_app_command=True, description="Output WeTheHobby Instagram", aliases=["ig", "insta"])
    async def instagram(self, ctx):
        '''
        Outputs WeTheHobby Instagram - [prefix]tiktok
        '''
        await ctx.send("https://www.instagram.com/wethehobby/", ephemeral=True)

    @commands.hybrid_command(name="twitter", with_app_command=True, description="Output WeTheHobby Twitter/X", aliases=["x"])
    async def twitter(self, ctx):
        '''
        Outputs WeTheHobby Twitter - [prefix]twitter
        '''
        await ctx.send("https://x.com/WeTheHobby", ephemeral=True)

    @commands.hybrid_command(name="facebook", with_app_command=True, description="Output WeTheHobby Facebook", aliases=["fbook"])
    async def facebook(self, ctx):
        '''
        Outputs WeTheHobby Facebook - [prefix]facebook
        '''
        await ctx.send("https://www.facebook.com/wethehobby/", ephemeral=True)

    @commands.hybrid_command(name="youtube", with_app_command=True, description="Output WeTheHobby YouTube", aliases=["yt"])
    async def youtube(self, ctx):
        '''
        Outputs WeTheHobby YouTube - [prefix]youtube
        '''
        await ctx.send("https://www.youtube.com/@wethehobby", ephemeral=True)

    @commands.hybrid_command(name="website", with_app_command=True, description="Output WeTheHobby Website")
    async def website(self, ctx):
        '''
        Outputs WeTheHobby Website - [prefix]website
        '''
        await ctx.send("https://www.youtube.com/@wethehobby", ephemeral=True)

    @commands.hybrid_command(name="tiktok", with_app_command=True, description="Output WeTheHobby TikTok", aliases=["tt"])
    async def tiktok(self, ctx):
        '''
        Outputs WeTheHobby TikTok - [prefix]tiktok
        '''
        await ctx.send("https://www.tiktok.com/@wethehobby", ephemeral=True)

    @commands.hybrid_command(name="whatnot", with_app_command=True, description="Output WeTheHobby Whatnot", aliases=["wnot"])
    async def whatnot(self, ctx):
        '''
        Outputs WeTheHobby Whatnot - [prefix]whatnot
        '''
        await ctx.send("https://www.whatnot.com/user/wethehobby", ephemeral=True)

    @commands.hybrid_command(name="fanaticslive", with_app_command=True, description="Output WeTheHobby Fanatics Live", aliases=["fanatics", "flive"])
    async def fanaticslive(self, ctx): 
        '''
        Outputs WeTheHobby Fanatics Live - [prefix]fanaticslive 
        '''
        await ctx.send("https://get.fanatics.live/X8WW/qoqkiwc3", ephemeral=True)  

    @commands.hybrid_command(name="discord", with_app_command=True, description="Output WeTheHobby Discord")
    async def discord(self, ctx): 
        '''
        Outputs WeTheHobby Discord - [prefix]discord 
        '''
        await ctx.send("https://discord.gg/wethehobby")  

    @commands.hybrid_command(name="socials", with_app_command=True, description="Output WeTheHobby Social Medias", aliases=["socialmedias", "socialmedia"])
    async def socials(self, ctx):
        '''
        Outputs WeTheHobby Socials - [prefix]socials
        '''
        embedVar = discord.Embed(title="WeTheHobby - Socials", color=0xA923CF)
        embedVar.add_field(name="Instagram", value="https://www.instagram.com/wethehobby/", inline=False)
        embedVar.add_field(name="Twitter", value="https://x.com/WeTheHobby", inline=False)
        embedVar.add_field(name="Facebook", value="https://www.facebook.com/wethehobby/", inline=False)
        embedVar.add_field(name="YouTube", value="https://www.youtube.com/@wethehobby", inline=False)
        embedVar.add_field(name="Discord", value="https://discord.gg/wethehobby", inline=False)
        embedVar.add_field(name="TikTok", value="https://www.tiktok.com/@wethehobby", inline=False)
        embedVar.add_field(name="Whatnot", value="https://www.whatnot.com/user/wethehobby", inline=False)
        embedVar.add_field(name="Fanatics Live", value="https://get.fanatics.live/X8WW/qoqkiwc3", inline=False)
        embedVar.add_field(name="Website", value="https://www.wethehobby.com", inline=False)
        await ctx.send(embed=embedVar, ephemeral=True)
        
async def setup (client):
    await client.add_cog(socials(client))
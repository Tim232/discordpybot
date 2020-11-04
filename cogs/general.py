from discord.ext import commands


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hello(self, ctx):
      await ctx.send("hello")
    
    @commands.command()
    async def developer(self, ctx):
        await ctx.send("`! Tim23#9999` 임돠ㅏ")
      
def setup(bot):
    bot.add_cog(general(bot))

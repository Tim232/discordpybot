from discord.ext import commands


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hello(self, ctx):
      await ctx.send("hello")
      
def setup(bot):
    bot.add_cog(general(bot))

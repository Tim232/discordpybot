from discord.ext import commands
import os
bot=commands.Bot(command_prefix='!")
for file in os.listidr('cogs'):
    if file.endswith(/.py'):
        bot.load_extension('cogs.'+file)
bot.run('token')

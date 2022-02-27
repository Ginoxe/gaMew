import discord
from discord.ext import commands
from liar_cog import liar_cog

bot = commands.Bot(command_prefix = '..')

bot.add_cog(liar_cog(bot))

with open('token.txt') as token:
    bot.run(token.readline())
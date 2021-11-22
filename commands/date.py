from discord.ext import commands
from api import dateColor, dateInfo
import discord

@commands.command(aliases=['date'])
async def dates(ctx, *args):
  embed=discord.Embed(
    title = f"📅  {dateInfo()}",
    color = dateColor()
  )
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(dates)
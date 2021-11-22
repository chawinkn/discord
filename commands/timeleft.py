from discord.ext import commands
from api import requestAPI
import discord

@commands.command(aliases=['countdown', 'tu'])
async def timeleft(ctx, *args):
  json_data = requestAPI('https://nextjs.chawinkn.repl.co/api/countdown')
  embed=discord.Embed(
    title = f"🌷  {json_data['days']} {json_data['hours']} {json_data['minutes']} {json_data['seconds']}",
    color = discord.Colour.magenta()
  )
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(timeleft)
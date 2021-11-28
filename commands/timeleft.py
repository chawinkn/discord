from discord.ext import commands
from helper import fetch
import discord

@commands.command(aliases=['countdown', 'tu'])
async def timeleft(ctx, *args):
  d = fetch('https://nextjs.chawinkn.repl.co/api/countdown')
  embed=discord.Embed(
    title = f"🌷  {d['days']} {d['hours']} {d['minutes']} {d['seconds']}",
    color = discord.Colour.magenta()
  )
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(timeleft)
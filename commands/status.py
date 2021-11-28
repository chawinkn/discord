from discord.ext import commands
import discord
import os

@commands.command(aliases=['stat', 'stats'])
async def status(ctx, *args):
  embed=discord.Embed(
    title = "📊  Bot Status Dashboard",
    url = os.getenv('STATS'),
    color = 0x2ecc71
  )
  embed.set_image(url="https://tokanoon.chawinkn.repl.co/icon/stats.png")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(status)
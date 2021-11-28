from discord.ext import commands
from helper import fetch
import discord

@commands.command()
async def quote(ctx):
  d = fetch('https://zenquotes.io/api/random')
  embed=discord.Embed(
    title = "✍️  Quotes For You",
    description = d[0]['q'],
    color = discord.Colour.blue()
  )
  embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embed.set_footer(text=f"-{d[0]['a']}")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(quote)
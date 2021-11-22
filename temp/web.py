from discord.ext import commands
import discord

@commands.command(aliases=['web', 'toKn', 'toKanoon'])
async def website(ctx):
  embed=discord.Embed(
    description = "**[toKanoon](https://toKanoon.chawinkn.repl.co)**\nเว็ปรวมโปรเจคง่ายๆ ขำๆ",
    color = discord.Colour.magenta()
  )
  embed.set_thumbnail(url="https://tokanoon.chawinkn.repl.co/icon/favicon.png")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(website)
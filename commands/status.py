from discord.ext import commands
import discord

@commands.command(aliases=['stat'])
async def status(ctx, *args):
  embed=discord.Embed(
    title = "📊  Bot Status Dashboard",
    url = "https://stats.uptimerobot.com/yAKwRU763l/789525808",
    color = 0x2ecc71
  )
  embed.set_image(url="https://tokanoon.chawinkn.repl.co/icon/stats.png")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(status)
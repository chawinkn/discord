from discord.ext import commands
from random import choice
import discord

with open("src/cheab.txt", "r", encoding="utf-8") as f:
  quote = [i.strip() for i in f]

@commands.command(aliases=['cheabs'])
async def cheab(ctx):
  colour = [0xf1c40f, 0xe91e63, 0x2ecc71, 0xe67e22, 0x3498db, 0x7289da]
  emoji = ["🐶","🐱","🙈","😆","😝","😏","🥳","🤗","😉","😬","🤔","🌝","❤️","👌🏻","🤏🏻"]
  embed=discord.Embed(
    title = f"{choice(emoji)}  {choice(quote)}",
    color = choice(colour)
  )
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(cheab)
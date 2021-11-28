from discord.ext import commands
from random import choice
import discord

f = open('src/movie.txt', 'r')
av = [i.strip() for i in f]
f.close()

@commands.command(aliases=['av', 'movie', 'jav', 'jp', 'japans'])
async def japan(ctx):
  movie = choice(av)
  sentence = choice(["ไงดูเรื่องนี้ไหม", "หรือเรื่องนี้ดี", "อันนี้ก็โอ(เคร)", "คือลือๆ", "บอกเลยว่าเด็ด"])
  link = f"https://www.google.com/search?q={movie}"

  embed=discord.Embed(
    title = f"🎬  {sentence}",
    description = f"** {movie} - [Search]({link}) **",
    color = discord.Colour.magenta()
  )
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(japan)
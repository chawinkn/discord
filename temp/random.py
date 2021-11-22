from discord.ext import commands
from random import choice
import discord

f = open('src/movie.txt', 'r')
av = [i.strip() for i in f]
f.close()

@commands.command(aliases=['ran', 'randoms'])
async def random(ctx):
  sentence = choice(["10 เรื่องคืนนี้", "คืนนี้ ยาวๆ", "คืนนี้ไม่ได้นอน"])
  movie_list = "||"
  for i in range(10):
    m_select = choice(av)
    movie_list += f"**{i+1}. {m_select} - [Search](https://www.google.com/search?q={m_select})**"
    av.remove(m_select)
    if i != 9:
      movie_list += "\n"
  movie_list += "||"

  embed=discord.Embed(
    title = f"🎬  {sentence} (18+)",
    description = movie_list,
    color = discord.Colour.magenta()
  )
  embed.set_footer(text=f"Requested by {ctx.message.author}")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(random)
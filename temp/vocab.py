import discord
from discord.ext import commands

@commands.command(aliases=['vocabulary', 'vocabs'])
async def vocab(ctx, *args):
  # with open("src/eng.txt", "r") as eng_file:
  #   eng = [i.strip() for i in eng_file]
  # with open("src/thai.txt", "r", encoding="utf-8") as thai_file:
  #   thai = [i.strip() for i in thai_file]
  # with open("src/vocab.txt", "a") as vocab_file:
  #   for i in range(len(eng)):
  #     vocab_file.write(f"{eng[i]} {thai[i]}\n")
  vocab = ""
  with open("src/vocab.txt", "r", encoding="utf-8") as vocab_file:
    for i in vocab_file:
      vocab += i

  embed=discord.Embed(
    title = "100 Must-Know words",
    description = vocab,
    color = discord.Colour.magenta()
  )
  embed.set_footer(text=f"Requested by {ctx.message.author}")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(vocab)
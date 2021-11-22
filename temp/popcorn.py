from discord.ext import commands

@commands.command()
async def popcorn(ctx):
  await ctx.message.delete()
  await ctx.send("https://tenor.com/view/popcorns-crackhead-eating-popcorn-food-junk-gif-14546221")

def setup(bot):
    bot.add_command(popcorn)
from discord.ext import commands

@commands.command()
async def debug(ctx):
    await ctx.send("https://f.ptcdn.info/114/052/000/os8vamgl4TQdXXSm2iI-o.jpg")

def setup(bot):
    bot.add_command(debug)
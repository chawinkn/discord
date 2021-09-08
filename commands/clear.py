from discord.ext import commands

@commands.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

def setup(bot):
    bot.add_command(clear)
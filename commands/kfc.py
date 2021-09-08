from discord.ext import commands
from random import choice

@commands.command()
async def kfc(ctx):
    await ctx.send(choice([
        'https://tenor.com/view/wrestling-kfc-chicken-gif-9769640', 'https://tenor.com/view/angek-kfc-party-gif-17959481', 'https://tenor.com/view/kfc-cristiano-ronaldo-chicken-fried-gif-7511530', 'https://tenor.com/view/kfc-chicken-bone-box-breasts-gif-12776930', 'https://tenor.com/view/colonel-colonel-sanders-dancing-queen-dancingcolonel-kfc-gif-12963709'
    ]))

def setup(bot):
    bot.add_command(kfc)
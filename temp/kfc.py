from discord.ext import commands
from random import choice
import discord

@commands.command()
async def kfc(ctx, user: discord.User=None):
    gif = [
        'https://tenor.com/view/wrestling-kfc-chicken-gif-9769640', 'https://tenor.com/view/angek-kfc-party-gif-17959481', 'https://tenor.com/view/kfc-cristiano-ronaldo-chicken-fried-gif-7511530', 'https://tenor.com/view/kfc-chicken-bone-box-breasts-gif-12776930', 'https://tenor.com/view/colonel-colonel-sanders-dancing-queen-dancingcolonel-kfc-gif-12963709'
    ]
    
    if not user:
        await ctx.send(f"<@{ctx.author.id}>")
        await ctx.send(choice(gif))
    else:
        await ctx.send(f"<@{user.id}>")
        await ctx.send(choice(gif))

def setup(bot):
    bot.add_command(kfc)
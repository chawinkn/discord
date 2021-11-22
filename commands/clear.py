from discord.ext import commands
import discord

@commands.command()
async def clear(ctx, *args):
  amount = int(args[0]) if len(args) else 5
  limits = 20 if amount > 20 else amount
  if ctx.message.author.guild_permissions.administrator:
    await ctx.channel.purge(limit=limits)
  else:
    embed = discord.Embed(
      title=f"😵  Error", 
      description="This command can only use by `user that have admin permission` or This bot `doesn't have admin permission`", colour=discord.Colour.gold()
    ) 
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(clear)
from discord.ext import commands
import discord

@commands.command(aliases=['roles'])
async def role(ctx):
  _r = sorted([str(r.name) for r in ctx.guild.roles if str(r.name)!="@everyone"])
  r = [_r[i]+"\n" if i != len(_r)-1 else _r[i] for i in range(len(_r))]
  roles = "".join(r)

  embed=discord.Embed(
    title = "🙎‍♂️  Roles in server",
    description = f"{roles}",
    color = discord.Colour.blue()
  )
  embed.set_footer(text=f"Requested by {ctx.message.author}")
  await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(role)
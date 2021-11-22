from discord.ext import commands
import discord

@commands.command(aliases=['si'])
async def info(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  icon = str(ctx.guild.icon_url)

  embed = discord.Embed(
    title = name + " Server Information",
    description = description,
    color = discord.Color.blue()
  )
  embed.set_thumbnail(url = icon)
  embed.add_field(name = "Owner", value = owner, inline = True)
  embed.add_field(name = "Server ID", value = id, inline = True)
  embed.add_field(name = "Region", value = region, inline = True)
  embed.add_field(name = "Member Count", value = memberCount, inline = True)
  embed.set_footer(text=f"Requested by {ctx.message.author}")
  await ctx.send(embed = embed)

def setup(bot):
  bot.add_command(info)
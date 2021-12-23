from discord.ext import commands
from helper import dateColor, bangkok
import discord

with open("src/subject.txt", "r", encoding="utf-8") as f:
  lst = [[j.strip() for j in i.split(" ", 11)] for i in f]

@commands.command(aliases=['class', 'schedule', 'c', 'sc'])
async def classes(ctx):
  d = bangkok().strftime("%a")
  h = bangkok().strftime("%H")
  m = bangkok().strftime("%M")

  day = ["Mon", "Tue", "Wed", "Thu", "Fri"]
  period = [
    ['0810', '0850'], ['0850', '0930'], 
    ['0930', '0940'], ['0940', '1020'], 
    ['1020', '1100'], ['1100', '1140'], 
    ['1140', '1220'], ['1220', '1230'], 
    ['1230', '1310'], ['1310', '1350'],
    ['1350', '1400'], ['1400', '1440']
  ]

  if d in day:
    this = lst[day.index(d)]
    for i in period:
      hr, mn = i[0], i[1]
      if int(h+m) in range(int(hr), int(mn)):
        embed=discord.Embed(
          title = f'📚  Class {period.index(i)+1} ({hr[:2]}:{hr[2:]} - {mn[:2]}:{mn[2:]} น.)',
          description = "สามารถดูตารางเรียนและข้อมูลอื่นๆ ได้ที่ https://bit.ly/3jRv1pQ",
          color = dateColor()
        )
        embed.add_field(
          name = "Subject : ", 
          value = f"{this[period.index(i)]}", 
          inline = True
        )
        embed.add_field(
          name = "Next : ",
          value = f"{this[period.index(i)+1] if period.index(i)+1 < len(this) else '-'}",
          inline = True
        )
        embed.set_image(url="https://tokanoon.chawinkn.repl.co/assets/images/schedule.png")
        embed.set_footer(text="**หมายเหตุ** - ลำดับของคาบเรียนอาจไม่ตรงกับตารางเรียน")
        await ctx.send(embed=embed)
        break
    else:
      embed = discord.Embed(
        title=f"🤔  There is no class right now", 
        description="แต่ให้ตารางไปก่อนละกัน",color=discord.Colour.gold()
      ) 
      embed.set_image(url="https://tokanoon.chawinkn.repl.co/assets/images/schedule.png")
      await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title=f"😬  There is no class today", 
      color=discord.Colour.gold()
    )
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(classes)
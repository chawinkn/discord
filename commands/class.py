from discord.ext import commands
from api import dateColor, bangkok
import discord

@commands.command(aliases=['class', 'schedule'])
async def classes(ctx):
  d = bangkok().strftime("%a")
  h = bangkok().strftime("%H")
  m = bangkok().strftime("%M")
  with open("src/subject.txt", "r", encoding="utf-8") as f:
    lst = [[j.strip() for j in i.split(" ", 11)] for i in f]
  day = ["Mon", "Tue", "Wed", "Thu", "Fri"]
  times = [
    ['0810', '0850'], ['0850', '0930'], 
    ['0930', '0940'], ['0940', '1020'], 
    ['1020', '1100'], ['1100', '1140'], 
    ['1140', '1220'], ['1220', '1230'], 
    ['1230', '1310'], ['1310', '1350'],
    ['1350', '1400'], ['1400', '1440']
  ]
  if d in day:
    this = lst[day.index(d)]
    for i in times:
      hr, mn = i[0], i[1]
      if int(h+m) in range(int(hr), int(mn)):
        nexts = this[times.index(i)+1] if times.index(i)+1 <= len(this) else "-"
        embed=discord.Embed(
          title = f'📚  Class {times.index(i)+1} ({hr[:2]}:{hr[2:]} - {mn[:2]}:{mn[2:]} น.)',
          description = "สามารถดูตารางเรียนและข้อมูลอื่นๆ ได้ที่ https://bit.ly/3jRv1pQ",
          color = dateColor()
        )
        embed.add_field(name="Subject : ", value=f"{this[times.index(i)]}", inline=True)
        embed.add_field(name="Next : ", value=str(nexts), inline=True)
        embed.set_image(url="https://tokanoon.chawinkn.repl.co/icon/schedule.png")
        embed.set_footer(text="**หมายเหตุ** - ลำดับของคาบเรียนอาจไม่ตรงกับตารางเรียน")
        await ctx.send(embed=embed)
        break
    else:
      embed = discord.Embed(
        title=f"😵  Error", 
        description="No classes more in this day or It's Not time yet", color=discord.Colour.gold()
      ) 
      await ctx.send(embed=embed)
  else:
    embed = discord.Embed(
      title=f"😵  Error", 
      description="No classes available in this day", 
      color=discord.Colour.gold()
    )
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(classes)
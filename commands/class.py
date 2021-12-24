from discord.ext import commands
from sheet import sheetData
from Time import timeCheck
from helper import dateColor, bangkok
import discord  

@commands.command(aliases=['class', 'schedule', 'c', 'sc'])
async def classes(ctx):
  currentTime = bangkok().strftime("%a %H %M").split()
  [day, hour, minute] = currentTime

  # You can edit excel file in src
  classData = sheetData(
    "src/schedule.xlsx", "B2:M6"
  )

  period =  [
    "08:10", "08:50",
    "09:30", "09:40",
    "10:20", "11:00",
    "11:40", "12:20",
    "12:30", "13:10",
    "13:50", "14:00",
    "14:40"
  ]

  classToday = classData[day]
  classIndex = timeCheck(
    hour, minute, period
  )
  classNow = classToday[classIndex]
  classRange = f"{period[classIndex]} - {period[classIndex + 1]} น."
  classNext = classToday[classIndex + 1] if classIndex + 1 < len(classToday) else "-"
  classNo =  classIndex + 1 if "พัก" not in classNow else "พัก"

  if day not in [*classData]:
    embed = discord.Embed(
      title = f"🤔  There is no classes in this day",
      color = discord.Colour.gold()
    )
    return await ctx.send(embed=embed)
  
  if classIndex == -1:
    embed = discord.Embed(
      title = f"🤔  There is no classes now",
      color = discord.Colour.gold()
    )
    await ctx.send(embed=embed)
    
  else:
    embed = discord.Embed(
      title = f'📚  Class {classNo} ({classRange})',
      description = "สามารถดูตารางเรียนและข้อมูลอื่นๆ ได้ที่ https://bit.ly/3jRv1pQ",
      color = dateColor()
    )
    embed.add_field(
      name = "Subject : ", 
      value = f"{classNow}", 
      inline = True
    )
    embed.add_field(
      name = "Next : ",
      value = f"{classNext}",
      inline = True
    )
    embed.set_image(url="https://tokanoon.chawinkn.repl.co/assets/images/schedule.png")
    embed.set_footer(text="**หมายเหตุ** - ลำดับของคาบเรียนอาจไม่ตรงกับตารางเรียน")
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(classes)
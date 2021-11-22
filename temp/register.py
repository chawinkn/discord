from discord.ext import commands
import discord
import os
import time

@commands.command()
async def register(ctx, *args):
  """
  Get data list from userdata.txt
  """
  # userdata = []
  # with open("data/userdata.txt", "r") as data_file:
  #   for i in data_file:
  #     userdata.append(i.strip().split(" ", 3))
  # print(userdata)
  start = time.time()
  d = {
    ctx.author.display_name: {
      "id": ctx.author.id,
      "time": time.time()-start
    }
  }
  print(d)

  # wd = os.getcwd()
  # folder_path = wd + '/data'
  # filelist = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
  # print(filelist)

def setup(bot):
  bot.add_command(register)
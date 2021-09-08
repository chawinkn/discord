from discord.ext import commands
import requests
import json

@commands.command()
async def dog(ctx):
    responce = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(responce.text)
    await ctx.send(json_data['message'])
 
def setup(bot):
    bot.add_command(dog)
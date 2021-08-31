import discord
import os
from discord.ext import commands
import requests
import json
from keep_alive import keep_alive
from random import choice

client = commands.Bot(command_prefix=os.getenv('PREFIX'))

def get_quote():
    responce = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(responce.text)
    quote = json_data[0]['q']
    author = json_data[0]['a']
    return [quote, author]

def get_dog():
    responce = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(responce.text)
    return json_data['message']

def set_embed(title, des, color, author, img, name, avatar):
    embed = discord.Embed(
        title=f"{title}" if title!=None else "",
        description=f"{des}" if des!=None else "",
        color=discord.Color.blue() if color=="blue" else discord.Colour.random()
    )
    if author != None:
        embed.set_footer(text=f"Requested by {author}")
    if img != None:
        embed.set_image(url=img)
    if name != None and avatar != None:
        embed.set_author(name=name, icon_url=avatar)
    return embed

@client.command()
async def github(ctx):
    await ctx.send("Read readme.md in https://github.com/chawinkn/discord")

@client.command()
async def howto(ctx):
    await ctx.send("Read readme.md in https://github.com/chawinkn/discord")

@client.command()
async def quote(ctx):
    text = get_quote()
    quote = text[0]
    author = text[1]
    embed=set_embed(
        "Quotes For You", quote, "blue", None, None, ctx.author.display_name, ctx.author.avatar_url
    )
    embed.set_footer(text=f"-{author}")
    await ctx.send(embed=embed)

@client.command()
async def dog(ctx):
    embed = discord.Embed()
    embed.set_image(url=get_dog())
    await ctx.send(embed=embed)

@client.command()
async def warp(ctx):
    f = open("src/movie.txt", "r")
    av = [i.strip() for i in f]
    movie = choice(av)
    sentence = ["ไงดูเรื่องนี้ไหม", "หรือเรื่องนี้ดี", "อันนี้ก็โอ(เคร)", "คือลือๆ", "บอกเลยว่าเด็ด"]
    image = ['https://i.ibb.co/T1m9W7b/19959314-102411923752581-434226783277558541-n.jpg']
    await ctx.send(embed=set_embed(
        "ขอให้ช่วยงั้นหรือ!", f"{choice(sentence)}\nName : ||**{movie} **||\nLink : ||**https://www5.javmost.com/{movie}/**||\nลิงค์ไหนเข้าไม่ได้ก็หาเอานะครับ\n (||**https://www.google.com/search?q={movie}**||)",
        "random", ctx.message.author, choice(image), ctx.author.display_name, ctx.author.avatar_url
    ))
    
@client.command()
async def table(ctx):
    await ctx.send(embed=set_embed(
        None, None, "blue", ctx.message.author, "https://cdn.discordapp.com/attachments/741297008618504216/872014022659166258/M312.jpg", ctx.author.display_name,
        ctx.author.avatar_url
    ))

@client.command()
async def add(ctx, *args):
    if 1 <= len(args) <= 2:
        f = open("src/source.txt", "a")
        name = args[0]
        link = args[-1] if args[-1][:8]=="https://" else ctx.message.attachments[0].url 
        f.write(f'{name} {link}\n')
        f.close()
        await ctx.send(embed=set_embed(
            "Add to list", f"Name: {name}\nLink: [View File]({link})", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))
        await ctx.message.delete()
    else:
        await ctx.send(embed=set_embed(
            "Error", "Please enter a correct input :heart:\nExample: $add name file", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))

@client.command()
async def update(ctx, *args):
    if 1 <= len(args) <= 2:
        f = open("src/source.txt", "r")
        name = args[0]
        link = args[-1] if args[-1][:8]=="https://" else ctx.message.attachments[0].url 
        data = []
        for i in f:
            raw = [j.strip() for j in i.split()]
            data.append(raw)
        f.close()
        f = open('src/source.txt', 'w')
        f.close()
        f = open("src/source.txt", "w")
        for i in data:
            if i[0]==name:
                f.write(f"{name} {link}\n")
            else:
                f.write(f"{i[0]} {i[1]}\n")
        f.close()
        await ctx.send(embed=set_embed(
            "Update file to list", f"Name: {name}\nLink: [View File]({link})", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))
        await ctx.message.delete()

    else:
        await ctx.send(embed=set_embed(
            "Error", "Please enter a correct input :heart:\nExample: $update name file", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))

@client.command()
async def remove(ctx, *args):
    f = open("src/source.txt", "r")
    data, data_name, data_link = [], [], []
    for i in f:
        raw = [j.strip() for j in i.split()]
        data.append(raw)
        data_name.append(raw[0])
        data_link.append(raw[1])
    f.close()

    if args[0] in data_name:
        name = args[0]
        link = data_link[data_name.index(name)]
        f = open('src/source.txt', 'w')
        f.close()
        f = open("src/source.txt", "w")
        for i in data:
            if i[0]!=name:
                f.write(f"{i[0]} {i[1]}\n")
        f.close()
        await ctx.send(embed=set_embed(
            "Delete file in list", f"Name: {name}\nOld Link: [View File]({link})", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))
        await ctx.message.delete()

    else:
        await ctx.send(embed=set_embed(
            "Error", "Please enter a correct input :heart:\nExample: $remove name", "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url
        ))

@client.command()
async def list(ctx, *args):
    f = open("src/source.txt", "r")
    data = []
    for i in f:
        raw = [j.strip() for j in i.split()]
        data.append(raw)

    data.sort()
    f.close()
    embed = discord.Embed(
        title='List',
        description="",
        color=discord.Color.blue()
    )
    embed = set_embed("List", None, "blue", ctx.message.author, None, ctx.author.display_name, ctx.author.avatar_url)
    for i in data:
        embed.add_field(name=i[0], value=f"[View File]({i[1]})", inline=True)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

keep_alive()
client.run(os.getenv('TOKEN'))
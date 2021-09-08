from discord.ext import commands
from random import choice
import discord

@commands.command(aliases=['av', 'movie', 'jav', 'jp', 'japans'])
async def japan(ctx):
    f = open('src/movie.txt', 'r')
    av = [i.strip() for i in f]
    movie = choice(av)
    sentence = choice(["ไงดูเรื่องนี้ไหม", "หรือเรื่องนี้ดี", "อันนี้ก็โอ(เคร)", "คือลือๆ", "บอกเลยว่าเด็ด"])
    link = f"https://www.google.com/search?q={movie}"
    # await ctx.reply(f"ว่าไง, {ctx.author.display_name}!\n{sentence} ||[{movie}]({link})||")
    embed=discord.Embed(
        title = f"🎬  {sentence}",
        description = f"** {movie} - [Search]({link}) **",
        color = discord.Colour.magenta()
    )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(japan)
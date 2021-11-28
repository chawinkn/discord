from discord.ext import commands

@commands.command()
async def prame(ctx):
  await ctx.send("https://lh3.googleusercontent.com/e1Wl8QVSd3wCGtIDGIFtqyfKeKjpQoL-XYq-Y-yghRdEsu3J0FHCnlFD9KYYE2fP_ojfb6c9nWLNbIIvci9wiFIZNR1ODfUfR9KbQtlctwcnDGhunLPdNe_hKaTcgU6_S9adz4-1Nw=w2400")
  await ctx.send("https://lh3.googleusercontent.com/y7kExG0dZJ1HQlQaFgxdoLej07APQk745fZ1MXN5_ZcIoJ3-eOW25qraYNhrDrQeGcyELal47IlRtbfNZTPoWtnV5Not-P_sj0qjchcYaY1CYi-BahqIfXIkhoYCtasu1YHJXQKvSA=w2400")

def setup(bot):
  bot.add_command(prame)
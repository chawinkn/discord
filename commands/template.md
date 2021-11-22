Default Template Code:
```python
from discord.ext import commands

@commands.command(aliases=['ชื่อ', '...'])
async def command_name(ctx, *args):
  # ทำทุกอย่างในนี้
  pass

def setup(bot):
  bot.add_command(command_name)
```

Embed Template Code:
```python
import discord

embed=discord.Embed(
  title = "หัวข้อ",
  description = "ข้อความ",
  color = discord.Colour.blue()
          or discord.Color.from_rgb(r, g, b)
)
embed.set_thumbnail(url="url")
# รูป Thumbnail
embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
# ชื่อ user รูป user
embed.set_footer(text=f"Requested by {ctx.message.author}")
# USERNAME#0000
await ctx.send(embed=embed)
```
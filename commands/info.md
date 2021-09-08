Template Code:
```python
from discord.ext import commands

@commands.command(aliases=['ชื่อ', '...'])
async def command_name(ctx, *args):
    # ทำทุกอย่างในนี้
    pass

def setup(bot):
    bot.add_command(command_name)
```
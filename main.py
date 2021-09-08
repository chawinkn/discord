import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
from command_loader import load
from helper import printList

os.system('clear')

# bot client
PREFIX = os.getenv('PREFIX')
client = commands.Bot(command_prefix=PREFIX,  help_command=None, case_insensitive=True)

# add command to client
error_module = load(client)
printList('Loaded command: ', client.walk_commands())

@commands.command()
async def help(ctx, *args):
    """Provides help information"""
    # this was eddited by vim gang ps.should'nt this break if the commnd is not found
    # await ctx.message.delete()
    # search for a command
    if len(args) != 0:
        commands_list = []

        for command in client.commands:
            commands_list.append({
                "name": command.name,
                "description": command.help,
                "aliases": command.aliases
            })

        command = next((command for command in commands_list if   command["name"] == args[0].lower() or args[0].lower() in set(command["aliases"])), None)

        if command:

            embed = discord.Embed(title="👨‍💻  {0}{1}".format(PREFIX, command["name"]), description=command["description"], colour=0xffffff)

            embed.add_field(name="👪  Aliases", value=", ".join(command["aliases"]) if len(command["aliases"]) != 0 else "-")

            embed.set_footer(text="type `{0}help` to get the list of all commands".format(PREFIX))

            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="😵  Error", description="help: command not found, type `{0}help` to get the list of all commands".format(PREFIX), colour=discord.Colour.gold())
            return await ctx.send(embed=embed)

    # just print out everything
    else:
        embed = discord.Embed(title="❔  Help", description="type {0}help <command> to get information about a command".format(PREFIX), colour=0xffffff)

        command_names = map(lambda name: "`{0}`".format(name),[command.name for command in client.commands])
        embed.add_field(name="📄  Commands", value=", ".join(command_names))

        await ctx.send(embed=embed)

client.add_command(help)

@client.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        embed = discord.Embed(title=f"😵  Error", description=f"command not found :(", color=discord.Colour.gold()) 
        await ctx.send(embed=embed)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

keep_alive()
client.run(os.getenv('TOKEN'))
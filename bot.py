# Imports
import os
import sys
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Loads variables from the .env file.
load_dotenv()
token = str(os.getenv('TOKEN'))
owner = int(os.getenv('OWNER'))

# Loads the discord bot
bot = discord.Bot()

# Creats command to print message
# when the bot is online.
@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready!')

def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)

# Example commands for the bot.
@bot.slash_command(name = "kill_count", description = "What?")
async def killcount(ctx: discord.ApplicationContext):
    await ctx.respond("13 currently missing, 0 found!")
    print(f'Killcount prompted by {ctx.author.name} (Id: {ctx.author.id})')

@bot.slash_command(name = "restart", description = "Restarts the robot. Self-explanatory.", hidden = True)
@commands.has_any_role('Clown Car Driver')
async def restart(ctx):
    await ctx.respond("Restarting!")
    print(f'Restart prompted by {ctx.author.name} (Id: {ctx.author.id}).\nRestarting...')
    restart_bot()

@bot.command(name = "shutdown", description = "Shuts down the robot. Don't use unless there's a problem!", hidden = True)
@commands.has_any_role('Clown Car Driver')
async def shutdown(ctx: discord.ApplicationContext):
    await ctx.respond("Shutting Down! Goodnight!")
    print(f'Shutdown prompted by {ctx.author.name} (Id: {ctx.author.id})')
    ctx.bot.close()

# Runs the bot.
bot.run(token)
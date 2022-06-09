import discord
import traceback
import sys
import os

from utilities.constants import ucursed
from discord.ext import commands, tasks
from itertools import cycle

# bot prefix
bot = commands.Bot(command_prefix = 'u-')

# bot status
status = cycle([ucursed.SEMESTER])

# cogs
initial_extensions = ['cogs.tests', 'cogs.status', 'cogs.help', 'cogs.horario']

# cogs loading
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()

# bot loaded
@bot.event
async def on_ready():
    change_status.start()
    print('U-Cursed ready for deployment.')

# loops bot status each hour (useless atm)
@tasks.loop(hours = 1)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# bot.run(YOUR_TOKEN)
bot.run(os.environ['token'])

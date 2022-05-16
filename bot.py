import discord
import traceback
import sys
import os
from discord.ext import commands, tasks
from itertools import cycle

# bot variables
bot = commands.Bot(command_prefix = 'U-')
semester = 'Primavera 2020 | U-Help'
status = cycle([semester + 'Salvando el semestre ʅʕ•ᴥ•ʔʃ', semester + 'Usando mascarilla ʕ º ᴥ ºʔ', semester + '#LoDamosVuelta ʕง•ᴥ•ʔง'])
initial_extensions = ['cogs.tests', 'cogs.status', 'cogs.help', 'cogs.trivial', 'cogs.subscription']

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

# add server to coursesData
@bot.event
async def on_guild_join(guild):
    server_id = str(guild.id)
    cm.addServerData(server_id)

# delete server from coursesData
@bot.event
async def on_guild_remove(guild):
    server_id = str(guild.id)
    cm.removeServerData(server_id)   

# loops bot status each hour
@tasks.loop(hours = 1)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# replace with your token
# bot.run(TOKEN)
bot.run(os.environ['token'])

import discord
from discord.ext import commands, tasks

# images
R = "https://i.ibb.co/qMMwwrb/R-de-color-Rojo.png"

# meme commands
class Trivial(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # image of an R
    @commands.command()
    @commands.guild_only()
    async def R(self, ctx):
        embed = discord.Embed(color = discord.Colour.red())
        embed.set_image(url = R)
        await ctx.send(embed=embed)

    # soy industrial
    @commands.command()
    @commands.guild_only()
    async def Pera(self, ctx):
        await ctx.message.add_reaction('\N{CALL ME HAND}')
        await ctx.send('¿ P o r  q u é  n o  s e  h a c e  i n d u s t r i a l ?')

    # letal
    @commands.command()
    @commands.guild_only()
    async def Letal(self, ctx):
        await ctx.send(':regional_indicator_l: :regional_indicator_e: :regional_indicator_t: :a: :regional_indicator_l:')

# cog loaded
def setup(bot):
    bot.add_cog(Trivial(bot))
    print('Trivial is loaded.')
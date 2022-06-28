import discord
from utilities.embed import embedPost
from utilities.constants.error import NO_COURSE
from discord.ext import commands, tasks

class Post(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # test for last post
    # TO DO: receive number of posts that user wants to see MAX 5
    @commands.command()
    @commands.guild_only()
    async def post(self, ctx, code, section):
        try:
            code = code.upper()
            embed = embedPost.notificationEmbed(code, section)
            await ctx.send(embed = embed)
        except:
            await ctx.send(content = NO_COURSE)

# cog loaded
def setup(bot):
    bot.add_cog(Post(bot))
    print('Post is loaded.')
import discord
from courses import coursesmgmt as cm
from courses import coursembed as ce
from discord.ext import commands, tasks

footerIcon = 'https://i.ibb.co/FmRwzfz/integrante.png'
footerText = 'by Polaris'

class Subscription(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # adds given course to course data
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Agrega(self, ctx, course, section):
        assert ctx.message.channel.name == 'u-cursos'

        server_id = str(ctx.message.guild.id)
        active_course = f'{course}-{section}'
        data = ce.notificationEmbed(course, section)

        if cm.courseInServerData(active_course, server_id):
            await ctx.send('Este curso ya ha sido agregado, si quieres eliminarlo ocupa **U-Elimina**.')

        elif data != False:
            cm.addCourseData(active_course, server_id)
            await ctx.send(f'**{data[1]}, Sección {section}** agregado correctamente.')
        
        else:
            await ctx.send('No se ha encontrado información del curso, ejecuta **U-Help** para más detalles.')           

    # removes given course from course data
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Elimina(self, ctx, course, section):
        assert ctx.message.channel.name == 'u-cursos'

        server_id = str(ctx.message.guild.id)
        active_course = f'{course}-{section}'

        if cm.courseInServerData(active_course, server_id):
            cm.removeCourseData(active_course, server_id)
            data = ce.notificationEmbed(course, section)
            courseName = data[1]
            await ctx.send(f'**{courseName}, Sección {section}** eliminado correctamente.')
            
        else:
            await ctx.send('El curso no ha sido agregado, si quieres agregarlo ocupa **U-Agrega**.')

    # returns embed with courses in the server
    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def Cursos(self, ctx):
        server_id = str(ctx.guild.id)
        server_name = ctx.guild.name
        courses = cm.activeCourses(server_id)
        embed = ce.coursesEmbed(server_name, courses)
        await ctx.send(embed = embed)

# cog loaded
def setup(bot):
    bot.add_cog(Subscription(bot))
    print('Subscription is loaded.')
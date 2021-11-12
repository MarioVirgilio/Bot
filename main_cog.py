import discord
import asyncio
import datetime
import json

from discord.ext import commands

f = open("rules.txt", "r")
rules = f.readlines()

class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Comandos Generales:
  !Help - Despliega todos los comandos disponibles
  !Regla <num> - Envía la regla específica 
  !Reglas - Despliega las reglas del server
  !Info <user> - Depliega la información del usuario
  !Server - Despliega la información del servidor
  !Avatar <user> - Manda la foto de perfil del usuario

Comandos para Admins:
  !K <user> - Expulsa a un usuario
  !Tempban <user> <cantidad> <unidad de tiempo> - Ban temporal a un usuario
  !Ban <user> - Banea a un usuario
  !Unban <user y id> - Desbanea a un usuario
  !C <num> - Borra un cantidad de mensajes específica

Comandos de la calculadora:
  !S <num1> <num2> - Suma 2 cantidades
  !R <num1> <num2> - Resta 2 cantidades
  !X <num1> <num2> - Multiplica 2 cantidades
  !D <num1> <num2> - Divide 2 cantidades
  !E <num1> <num2> - Exponencia un número en una cantidad deseada
  !E2 <num> - Exponencia al cuadrado un numero
  !E3 <num> - Exponencia al cubo un numero

Music commands:
  No disponible

Otros comandos:
  !Golpe <user> - Manda un gif a ese usuario
  !Apreton <user> - Manda un gif a ese usuario
  !Azar <pregunta> - Responde al azar una pregunta
  !Moneda - Tira una moneda
  !Dado6 - Tira un dado de 6 caras
  !DobleDado - Tira 2 dados de 6 caras
  !Carta - Manda una carta al azar 
  !Ctm
  !Mlp
  !Zokram
  !Skmlla
  !Yossef
  !Over

```
"""
        self.text_channel_list = []
      

    # Lista de comandos
    @commands.command(name="Help", aliases=['Ayuda', 'ayuda', 'help'], help="Desplega todos los comandos disponibles")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)


    # Expulsar usuario
    @commands.command(name="Expulsar", aliases=['k', 'K', 'expulsar '], help="Expulsa a un usuario")
    @commands.has_permissions(kick_members=True)
    async def expulsar(self, ctx, member: discord.Member, *, reason="Sin ninguna razón en particular"):
        try:
            await member.send(
                "Regresa a fornite fan de la CQ te kickeamos porque: " + reason)
        except:
            await ctx.send("El miembro tiene sus Dm's cerrados")

        await member.kick(reason=reason)


    # Ban temporal
    class DurationConverter(commands.Converter):
      async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['s', 'm']:
          return int(amount), unit

        raise commands.BadArgument(message='Duracion no valida')


    @commands.command(name="Tempban", aliases=['tempban', 'banTemp', 'Bantemp'], help="Ban temporal a un usuario")
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter):
    
        multiplier = {'s': 1, 'm': 60}
        amount, unit = duration

        await ctx.guild.ban(member)
        await ctx.send(f'{member} has sido baneado temporalmente por {amount}{unit}.')
        await asyncio.sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)


    # Banear usuario
    @commands.command(name="Ban", aliases=['ban', 'Banamex', 'banamex'], help="Banea a un usuario")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *,reason="Sin ninguna razón en particular"):
        await member.send(member.name + "Regresa a fornite fan de la CQ te baneamos porque: " + reason)
        await member.ban(reason=reason)


    # Quitar ban a usuario
    @commands.command(name="Unban", aliases=['unban', 'unb', 'Unb'], help="Desbanea a un usuario")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(member_name + " ha sido desbaneado")
                return
        await ctx.send(member_name + " no fue encontrado")


  # Mutear a usuario
  #  @commands.command(aliases=['m'])
  #  @commands.has_permissions(kick_members=True)
  #  async def mute(self, ctx, member: discord.Member):
  #      muted_role = ctx.guild.get_role(900403284181917726)

  #      await member.add_roles(muted_role)

  #      await ctx.send(member.mention + " ha sido muteado")


  #   Desmutear usuario
  #  @commands.command(name='unmute', aliases=['unm'])
  #  @commands.has_permissions(kick_members=True)
  #  async def unmute(self, ctx, member: discord.Member):
  #      muted_role = ctx.guild.get_role(900403284181917726)

  #      await member.remove_roles(muted_role)

  #      await ctx.send(member.mention + " ha sido desmuteado")


    # Borrar mensajes
    @commands.command(name="Clear", aliases=['c', 'C', 'clear'], help="Borra un cantidad de mensajes específica")
    @commands.has_permissions(ban_members=True)
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)


    # Regla específica
    @commands.command(name="Regla", aliases=['regla', 'Rule', 'rule'], help="Envía la regla específica")
    async def regla(self, ctx, *, number):
        await ctx.send(rules[int(number) - 1])
        

    # Reglas
    @commands.command(name="Reglas", aliases=['reglas', 'Rules', 'rules'], help="Despliega las reglas del server")
    async def reglas(self, ctx):
        response = 'Estas son las reglas del server' \
                  '\n\n:one: Mandar pack obligatorio para entrar en confianza. ' \
                  '\n:two: Usar NGE en el Nombre tanto en DL como en Discord gei el que no lo use.' \
                  '\n:three: Mandar a chingar a su madre a U7 y al zeroTG ' \
                  '\n:four: Evitar salirse del grupo general, de lo contrario serán acreedores a una Sanción.'

        categorias_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        categorias_embed.add_field(name="Reglas | :exclamation:", value=f"{response}")
        await ctx.send(embed=categorias_embed)
      
    
    # Información de usuario
    @commands.command(name="User", aliases=['user', 'Info', 'info'], help="Depliega la información del usuario")
    async def info(self, ctx, member: discord.Member):
        embed = discord.Embed(title=member.name, description=member.mention, color=discord.Color.green())
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)


    # Info del server
    @commands.command(name="Discord", aliases=['discord', 'Server', 'server'], help="Despliega la información del servidor")
    async def server(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}",timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=ctx.guild.icon_url)

        await ctx.send(embed=embed)
   
    
    # Avatar de perfil
    @commands.command(name="Avatar", aliases=['avatar', 'Perfil', 'perfil'], help="Manda la foto de perfil del usuario")
    async def avatar(self, ctx):

        args = ctx.message.content.split(" ")[1:]

        embed = discord.Embed()
        embed.colour = discord.Color.from_rgb(0, 255, 255)

        if len(args) == 0:
            embed.title = ctx.author.name
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif len(ctx.message.mentions) > 0:
            for member in ctx.message.mentions:
                embed.title = member.name
                embed.set_image(url=member.avatar_url)
                await ctx.send(embed=embed)

        elif args[0] in ("server", "guild"):
            embed.title = ctx.guild.name
            embed.set_image(url=ctx.guild.icon_url)
            await ctx.send(embed=embed)



    

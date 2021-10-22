import discord
import os
import random
import urllib.request
import json
from random import choice
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'

bot = commands.Bot(command_prefix=PREFIX)

f = open("rules.txt", "r")
rules = f.readlines()

filtered_words = ["zero", "Laxus", "PKM"]

cartas = [
    'https://static.wikia.nocookie.net/yugiohenespanol/images/d/dd/Foto_n%C3%BAmero_39_utop%C3%ADa.jpg/revision/latest?cb=20120122053915&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/58/Foto_mago_oscuro.jpg/revision/latest?cb=20120121043211&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/55/Foto_h%C3%A9roe_elemental_neos.jpg/revision/latest?cb=20120202055949&path-prefix=es',
    'https://static.zerochan.net/Odd-Eyes.Pendulum.Dragon.full.3210952.jpg',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/b/b6/Foto_decodificador_hablador.jpg/revision/latest?cb=20170321191013&path-prefix=es'
]


@bot.event  # Inicio
async def on_ready():
    print("Bot is ready")


@bot.event  # Filtro de palabras
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
    if ":" == msg.content[0] and ":" == msg.content[-1]:
        emoji_name = msg.content[1:-1]
        for emoji in msg.guild.emojis:
            if emoji_name == emoji.name:
                await msg.channel.send(str(emoji))
                await msg.delete()
                break
    if "fuck" in msg.content:
        await msg.add_reaction("<:Fuck:765783371167039548>")

    await bot.process_commands(msg)


@bot.event  # Mensaje de error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No puedes hacer eso")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor agrega los argumentos faltantes")
        await ctx.message.delete()
    else:
        raise error


@bot.command(aliases=['rule'])  # Regla específica
async def regla(ctx, *, number):
    await ctx.send(rules[int(number) - 1])


@bot.command(aliases=['rules'])  # Reglas
async def reglas(ctx):
    response = ":one: Mandar pack obligatorio para entrar en confianza. " \
               "\n:two: Usar NGE en el Nombre tanto en DL como en Discord gei el que no lo use." \
               "\n:three: Mandar a chingar a su madre a U7 y al zeroTG " \
               "\n:four: Evitar salirse del grupo general, de lo contrario serán acreedores a una Sanción."
    await ctx.send(response)


@bot.command(aliases=['c', 'clean', 'b', 'borra'])  # Borrar mensajes
@commands.has_permissions(manage_messages=True)
async def borrar(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@bot.command(aliases=['k', 'kick'])  # Expulsar usuario
@commands.has_permissions(kick_members=True)
async def expulsar(ctx, member: discord.Member, *, reason="Sin ninguna razón en particular"):
    try:
        await member.send("Regresa a fornite fan de la CQ te kickeamos porque: " + reason)
    except:
        await ctx.send("El miembro tiene sus Dm's cerrados")

    await member.kick(reason=reason)


@bot.command(aliases=['banamex'])  # Banear usuario
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Sin ninguna razón en particular"):
    await member.send(member.name + "Regresa a fornite fan de la CQ te baneamos porque: " + reason)
    await member.ban(reason=reason)


@bot.command(aliases=['unb'])  # Quitar ban a usuario
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " ha sido desbaneado")
            return
    await ctx.send(member_name + " no fue encontrado")


@bot.command(aliases=['m'])  # Mutear a usuario
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(900403284181917726)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " ha sido muteado")


@bot.command(name='umute', aliases=['unm'])  # Desmutear usuario
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(900403284181917726)

    await member.remove_roles()

    await ctx.send(member.mention + " ha sido desmuteado")


@bot.command()  # Avatar de perfil
async def avatar(ctx):
    # Obtenemos los argumentos del mensaje que serán usados posteriormente
    args = ctx.message.content.split(" ")[1:]

    # Preparamos el embed que mostrara la imagen
    embed = discord.Embed()
    embed.colour = discord.Color.from_rgb(0, 255, 255)

    # Avatar propio, cuando no hay ningún argumento
    if len(args) == 0:
        embed.title = ctx.author.name
        embed.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    # Avatar de los mencionados, cuando se detecten menciones en el mensaje
    elif len(ctx.message.mentions) > 0:
        for member in ctx.message.mentions:
            embed.title = member.name
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

    # Avatar del server, cuando el primer argumento sea 'server' o 'guild'
    elif args[0] in ("server", "guild"):
        embed.title = ctx.guild.name
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    # En caso de dar un argumento incorrecto el bot mostrara su correcto uso
    else:
        embed.title = "avatar"
        embed.description = f"Muestra tu avatar, de los usuarios mencionados o del servidor."
        embed.add_field(name="Uso:", value=f"{PREFIX}avatar\n{PREFIX}avatar @user1, @user2, ...\n{PREFIX}avatar server",
                        inline=False)
        await ctx.send(embed=embed)


@bot.command(aliases=['azar'])  # Azar
async def bola8(ctx, *, question):
    response = ['En mi opinión, sí',
                'Es cierto',
                'Es decididamente así',
                'Probablemente',
                'Buen pronóstico',
                'Todo apunta a que sí',
                'Sin duda',
                'Sí',
                'Sí - definitivamente',
                'Debes confiar en ello',
                'Respuesta vaga, vuelve a intentarlo',
                'Pregunta en otro momento',
                'Será mejor que no te lo diga ahora',
                'No puedo predecirlo ahora',
                'Concéntrate y vuelve a preguntar',
                'Puede ser',
                'No cuentes con ello',
                'Mi respuesta es no',
                'Mis fuentes me dicen que no',
                'Las perspectivas no son buenas',
                'Muy dudoso']
    _8ball_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    _8ball_embed.add_field(name="Comando Azar | :8ball:",
                           value=f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}")
    await ctx.send(embed=_8ball_embed)


@bot.command(aliases=['toss'])  # Moneda
async def moneda(ctx):
    response = ['Cara',
                'Cruz']
    moneda_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    moneda_embed.add_field(name="Comando Moneda | :coin:",
                           value=f"{random.choice(response)}")
    await ctx.send(embed=moneda_embed)


@bot.command(aliases=['roll6'])  # Dado
async def dado6(ctx):
    response = [':one:',
                ':two:',
                ':three:',
                ':four:',
                ':five:',
                ':six:']
    dado_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    dado_embed.add_field(name="Comando Dado | :ice_cube:", value=f"{random.choice(response)}")
    await ctx.send(embed=dado_embed)


@bot.command(aliases=['2roll6', '2dado6'])  # Dado
async def dado(ctx):
    response = [':one:-:one:', ':one:-:two:', ':one:-:three:', ':one:-:four:', ':one:-:five:', ':one:-:six:',
                ':two:-:one:', ':two:-:two:', ':two:-:three:', ':two:-:four:', ':two:-:five:', ':two:-:six:',
                ':three:-:one:', ':three:-:two:', ':three:-:three:', ':three:-:four:', ':three:-:five:',
                ':three:-:six:',
                ':four:-:one:', ':four:-:two:', ':four:-:three:', ':four:-:four:', ':four:-:five:', ':four:-:six:',
                ':five:-:one:', ':five:-:two:', ':five:-:three:', ':five:-:four:', ':five:-:five:', ':five:-:six:',
                ':six:-:one:', ':six:-:two:', ':six:-:three:', ':six:-:four:', ':six:-:five:', ':six:-:six:']
    dado_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    dado_embed.add_field(name="Comando Dado | :ice_cube:", value=f"{random.choice(response)}")
    await ctx.send(embed=dado_embed)


@bot.command(aliases=['rate'])  # Rate/Calificar
async def _rate_embed(ctx, *, question):
    response = ['0/10',
                '1/10',
                '2/10',
                '3/10',
                '4/10',
                '5/10',
                '6/10',
                '7/10',
                '8/10',
                '9/10',
                '10/10',
                '9/11 bruh']
    rate_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    rate_embed.add_field(name="Comando Rate | :100:",
                         value=f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}")
    await ctx.send(embed=rate_embed)


@bot.command(name='golpe', aliases=['punch'])  # Golpe
async def golpe(ctx, *, member: discord.Member):
    listGifs = ['https://c.tenor.com/DMWqIb2Rdp4AAAAi/bonk-cheems.gif',
                'https://c.tenor.com/cqnZ1RW_XjsAAAAC/horny-bonk.gif',
                'https://c.tenor.com/O0XLzUO24X4AAAAC/sape-golpear.gif',
                'https://c.tenor.com/JEvWuCTiIZcAAAAC/sape-un.gif',
                'https://c.tenor.com/PTONt_7DUTgAAAAC/batman-slap-robin.gif',
                'https://c.tenor.com/gFqmPEMWqEQAAAAC/the-simpsons-homer-simpson.gif',
                'https://c.tenor.com/XhdHGRof6WEAAAAC/anime-ataque-golpe-en-la-pared.gif']
    punch_embed = discord.Embed(title='  ',
                                description=f"**{member}** te envía un madrazo el usuario **{ctx.author}** por retard",
                                color=discord.Color.blue())
    punch_embed.set_image(url=random.choice(listGifs))
    await ctx.send(embed=punch_embed)


@bot.command(name='apreton', aliases=['handshake'])  # Apreton
async def apreton(ctx, *, member: discord.Member):
    listGifs = ['https://c.tenor.com/9t3luBDOyHEAAAAC/the-simpsons-simpson.gif',
                'https://c.tenor.com/qcYlFf9IyQ8AAAAC/dap-handshake.gif',
                'https://c.tenor.com/ytbz1Epg7Q8AAAAC/predator-arnold.gif',
                'https://c.tenor.com/jkRs8LGfq0oAAAAd/hulk-hogan-shake-hands.gif',
                'https://c.tenor.com/5m5QGsVqkR8AAAAC/shake-hands-tom-and-jerry.gif,'
                'https://c.tenor.com/c-G2PhTsLQAAAAAC/handshake-deal.gif',
                'https://c.tenor.com/kPbvjinMD_0AAAAC/manly-handshake-fma-brotherhood.gif',
                'https://c.tenor.com/rmklzHMYy80AAAAC/nichijou-anime.gif',
                'https://c.tenor.com/IpL5xXxRiyoAAAAC/fresh-prince-handshake.gif',
                'https://c.tenor.com/JnYWuwU3c_YAAAAd/fist-bump-hand-shake.gif',
                'https://c.tenor.com/cwcnDr805qoAAAAC/handshake-black-ranger.gif',
                'https://c.tenor.com/sJhQNrxE-pMAAAAC/the-simpsons-homer-simpson.gif'
                ]
    hand_embed = discord.Embed(title='  ', description=f"**{member}** hombre de cultura **{ctx.author}**",
                               color=discord.Color.blue())
    hand_embed.set_image(url=random.choice(listGifs))
    await ctx.send(embed=hand_embed)


@bot.command(aliases=['user', 'info'])
# @commands.has_permissions(kick_members=True)
async def avers(ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Color.green())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@bot.command()
async def carta(ctx):
    embed = discord.Embed(color=discord.Color.red())
    random_link = random.choice(cartas)
    embed.set_image(url=random_link)
    await ctx.send(embed=embed)


@bot.command(name='mlp')
async def mlp(ctx):
    response = "@AxwellG NGE#4759 está bien pendejo :100:"
    await ctx.send(response)


@bot.command(name='Zokram')
async def zokram(ctx):
    response = "Vamos Zokram habla como loli"
    await ctx.send(response)


@bot.command(name='Skmlla')
async def skmlla(ctx):
    response = "Camara Saquen el WildRift"
    await ctx.send(response)


@bot.command(name='Yossef')
async def yossef(ctx):
    response = "Callese viejo ridiculo"
    await ctx.send(response)


@bot.command(name='Over')
async def over(ctx):
    response = "Te quiero papi"
    await ctx.send(response)


@bot.command(name='ctm')
async def ctm(ctx):
    await ctx.send("ctm mamón <:Fuck:765783371167039548>")


bot.run(TOKEN)

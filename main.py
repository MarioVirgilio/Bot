import discord
import os
import random
from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
status = cycle(['With ur mom', 'Gay el que lo lea', 'Sus', 'DB super es para pendejos'])

bot = commands.Bot(command_prefix=PREFIX)

f = open("rules.txt", "r")
rules = f.readlines()

filtered_words = ["Laxus", "laxus", "PKM","pkm"]

cartas = [
    'https://static.wikia.nocookie.net/yugiohenespanol/images/d/dd/Foto_n%C3%BAmero_39_utop%C3%ADa.jpg/revision/latest?cb=20120122053915&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/58/Foto_mago_oscuro.jpg/revision/latest?cb=20120121043211&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/55/Foto_h%C3%A9roe_elemental_neos.jpg/revision/latest?cb=20120202055949&path-prefix=es',
    'https://static.zerochan.net/Odd-Eyes.Pendulum.Dragon.full.3210952.jpg',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/b/b6/Foto_decodificador_hablador.jpg/revision/latest?cb=20170321191013&path-prefix=es'
]


# Inicio
@bot.event
async def on_ready():
  change_status.start()
  print("Bot is ready")


@tasks.loop(minutes=3)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))


# Filtro de palabras
@bot.event
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
    if "zokram" in msg.content:
        await msg.add_reaction("<:Simp:792898073214582785>")
    if "axwell" in msg.content:
        await msg.add_reaction("<:Srave:765407853091356683>")
    if "yossef" in msg.content:
        await msg.add_reaction("<:Fuck:765783371167039548>")
    await bot.process_commands(msg)


# Mensaje de error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("No puedes hacer eso")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Por favor agrega los argumentos faltantes")
        await ctx.message.delete()
    else:
        raise error


# Categorías
@bot.command(aliases=['commands', 'ayuda', 'Ayuda'])
async def comandos(ctx):
    response = 'Hola mi Nombre es Chad Bot, soy la creación de over, hasta ahora estos son las categorías de funciones que tengo: ' \
               '\n\n:red_circle:Comandos de Admin:-------------"!admin" para ver mas info.' \
               '\n:red_circle:Comandos de Calculadora:-------"!calculadora" para ver mas info.' \
               '\n:red_circle:Comandos Generales:------------"!generales" para ver mas info.' \
               '\n:red_circle:Comandos Memes:---------------"!memes" para ver mas info.'

    categorias_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    categorias_embed.add_field(name="Categorías | :exclamation:", value=f"{response}")
    await ctx.send(embed=categorias_embed)


# Administrador
@bot.command(aliases=['Admin'])
async def admin(ctx):
    response = 'Estos son los comandos para administardores: ' \
               '\n\n:x:Expulsar usuario:--------"!kick".' \
               '\n:x:Banear usuario:----------"!ban".' \
               '\n:x:Desbanear usuario:-----"!unban".' \
               '\n:x:Mutear usuario:---------"!mute".' \
               '\n:x:Desmutear usuario:-----"!unmute".'\
               '\n:x:Borrar mensajes:--------"!c".'

    admin_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.red())
    admin_embed.add_field(name="Admin | :exclamation:", value=f"{response}")
    await ctx.send(embed=admin_embed)


# General
@bot.command(aliases=['General'])
async def general(ctx):
    response = 'Estos son los comandos generales: ' \
               '\n\n:small_orange_diamond:Categorías de comandos:-----"!ayuda".' \
               '\n:small_orange_diamond:Buscar Regla:-------------------"!regla".' \
               '\n:small_orange_diamond:Leer Reglas:--------------------"!reglas".' \
               '\n:small_orange_diamond:Ver Avatar:---------------------"!avatar".'\
               '\n:small_orange_diamond:Elección al Azar:---------------"!azar".'\
               '\n:small_orange_diamond:Tiro de Moneda:---------------"!moneda".'\
               '\n:small_orange_diamond:Tiro de Dado:------------------"!dado6".'\
               '\n:small_orange_diamond:Doble Dado:-------------------"!2dado6".'\
               '\n:small_orange_diamond:Calificar algo:------------------"!rate".'\
               '\n:small_orange_diamond:Información de usuario:-------"!info".'

    general_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.dark_gold())
    general_embed.add_field(name="General | :exclamation:", value=f"{response}")
    await ctx.send(embed=general_embed)


# Calculadora
@bot.command(aliases=['Calculadora', 'calculadora'])
async def mate(ctx):
    response = 'Estos son los comandos matemáticos: ' \
               '\n\n:green_circle: Sumar:------------------"!S".' \
               '\n:green_circle: Restar:------------------"!R".' \
               '\n:green_circle: Multiplicar-------------"!X".' \
               '\n:green_circle: Exponencial:-----------"!E".'\
               '\n:green_circle: Cuadrado:--------------"!E2".'\
               '\n:green_circle: Cubo:-------------------"!E3".'\
               '\n:green_circle: Dividir:-----------------"!D".'

    categorias_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.green())
    categorias_embed.add_field(name="Calculadora | :exclamation:", value=f"{response}")
    await ctx.send(embed=categorias_embed)

# Memes
@bot.command(aliases=['Memes', 'memes', 'Meme'])
async def meme(ctx):
    response = 'Estos son los comandos matemáticos: ' \
               '\n\n:black_square_button: Golpe:------------------"!golpe".' \
               '\n:black_square_button: Apreton:---------------"!apreton".' \
               '\n:black_square_button: Carta-------------------"!carta".' \
               '\n:black_square_button: Mlp:--------------------"!mlp".'\
               '\n:black_square_button: Simp:-------------------"!zokram".'\
               '\n:black_square_button: Wild Rift:--------------"!skmlla".'\
               '\n:black_square_button: Franz:------------------"!yossef".'\
               '\n:black_square_button: Yo:---------------------"!over".'\
               '\n:black_square_button: CTM:------------------"!ctm".'\

    memes_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blurple())
    memes_embed.add_field(name="Calculadora | :exclamation:", value=f"{response}")
    await ctx.send(embed=memes_embed)

# Regla específica
@bot.command(aliases=['rule'])
async def regla(ctx, *, number):
    await ctx.send(rules[int(number) - 1])


# Reglas
@bot.command(aliases=['rules'])
async def reglas(ctx):
    response = ":one: Mandar pack obligatorio para entrar en confianza. " \
               "\n:two: Usar NGE en el Nombre tanto en DL como en Discord gei el que no lo use." \
               "\n:three: Mandar a chingar a su madre a U7 y al zeroTG " \
               "\n:four: Evitar salirse del grupo general, de lo contrario serán acreedores a una Sanción."
    await ctx.send(response)


# Borrar mensajes
@bot.command(aliases=['c', 'clean', 'b'])
@commands.has_permissions(kick_members=True)
async def borrar(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


# Expulsar usuario
@bot.command(aliases=['k', 'kick'])
@commands.has_permissions(kick_members=True)
async def expulsar(ctx, member: discord.Member, *, reason="Sin ninguna razón en particular"):
    try:
        await member.send("Regresa a fornite fan de la CQ te kickeamos porque: " + reason)
    except:
        await ctx.send("El miembro tiene sus Dm's cerrados")

    await member.kick(reason=reason)


# Banear usuario
@bot.command(aliases=['banamex'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Sin ninguna razón en particular"):
    await member.send(member.name + "Regresa a fornite fan de la CQ te baneamos porque: " + reason)
    await member.ban(reason=reason)


# Quitar ban a usuario
@bot.command(aliases=['unb'])
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


# Mutear a usuario
@bot.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(900403284181917726)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " ha sido muteado")


# Desmutear usuario
@bot.command(name='unmute', aliases=['unm'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(900403284181917726)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " ha sido desmuteado")


# Avatar de perfil
@bot.command(aliases=['perfil'])
async def avatar(ctx):

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

    else:
        embed.title = "avatar"
        embed.description = f"Muestra tu avatar, de los usuarios mencionados o del servidor."
        embed.add_field(name="Uso:", value=f"{PREFIX}avatar\n{PREFIX}avatar @user1, @user2, ...\n{PREFIX}avatar server",
                        inline=False)
        await ctx.send(embed=embed)


# Azar
@bot.command(aliases=['azar'])
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


# Moneda
@bot.command(aliases=['toss'])
async def moneda(ctx):
    response = ['Cara',
                'Cruz']
    moneda_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    moneda_embed.add_field(name="Comando Moneda | :coin:",
                           value=f"{random.choice(response)}")
    await ctx.send(embed=moneda_embed)


# Dado
@bot.command(aliases=['roll6'])
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


# Dos dados de seis caras
@bot.command(aliases=['2roll6', '2dado6'])
async def dado(ctx):
    response = [':one:-:one:', ':one:-:two:', ':one:-:three:', ':one:-:four:', ':one:-:five:', ':one:-:six:',
                ':two:-:one:', ':two:-:two:', ':two:-:three:', ':two:-:four:', ':two:-:five:', ':two:-:six:',
                ':three:-:one:', ':three:-:two:', ':three:-:three:', ':three:-:four:', ':three:-:five:', ':three:-:six:',
                ':four:-:one:', ':four:-:two:', ':four:-:three:', ':four:-:four:', ':four:-:five:', ':four:-:six:',
                ':five:-:one:', ':five:-:two:', ':five:-:three:', ':five:-:four:', ':five:-:five:', ':five:-:six:',
                ':six:-:one:', ':six:-:two:', ':six:-:three:', ':six:-:four:', ':six:-:five:', ':six:-:six:']
    dado_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
    dado_embed.add_field(name="Comando Dado | :ice_cube:", value=f"{random.choice(response)}")
    await ctx.send(embed=dado_embed)


# Rate/Calificar
@bot.command(aliases=['rate'])
async def calificar(ctx, *, question):
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


# Golpe
@bot.command(name='golpe', aliases=['punch'])
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


# Apreton
@bot.command(name='apreton', aliases=['handshake'])
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


# Información de usuario
@bot.command(aliases=['user', 'info'])
async def avers(ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Color.green())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


# Carta al azar
@bot.command(aliases=['card','Card', 'Carta'])
async def carta(ctx):
    embed = discord.Embed(color=discord.Color.red())
    random_link = random.choice(cartas)
    embed.set_image(url=random_link)
    await ctx.send(embed=embed)


@bot.command(name='mlp', aliases=['MLP'])
async def mlp(ctx):
    response = "@AxwellG NGE#4759 está bien pendejo :100:"
    await ctx.send(response)


@bot.command(name='Zokram', aliases=['zokram'])
async def zokram(ctx):
    response = "Vamos Zokram habla como loli"
    await ctx.send(response)


@bot.command(name='Skmlla', aliases=['skmlla'])
async def skmlla(ctx):
    response = "Camara Saquen el WildRift"
    await ctx.send(response)


@bot.command(name='Yossef', aliases=['yossef'])
async def yossef(ctx):
    response = "Callese viejo ridiculo"
    await ctx.send(response)


@bot.command(aliases=['Over'])
async def over(ctx):
    response = "Te quiero papi <:mmmm:765440193217822742>"
    await ctx.send(response)


@bot.command(name='ctm', aliases=['CTM'])
async def ctm(ctx):
    await ctx.send("ctm mamón <:Fuck:765783371167039548>")


# Suma
@bot.command(aliases=['S', 's', 'Sumar'])
async def sumar(ctx, var1,var2):
    response = int(var1)+int(var2)
    statement = ("La suma de "+str(var1)+"+"+str(var2)+" es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Resta
@bot.command(aliases=['R', 'r', 'Restar'])
async def restar(ctx, var1,var2):
    response = int(var1)-int(var2)
    statement = ("La resta de " + str(var1) + "-" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Multiplicar
@bot.command(aliases=['X', 'x', 'Multiplicar'])
async def multiplicar(ctx, var1,var2):
    response = int(var1)*int(var2)
    statement = ("La multiplicacion de " + str(var1) + "*" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Exponencial
@bot.command(aliases=['E', 'e', 'exponencial', 'Exponencial', 'Exp'])
async def exp(ctx, var1,var2):
    response = int(var1)**int(var2)
    statement = ("El numero " + str(var1) + "^" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Cuadrado
@bot.command(aliases=['e2', 'E2'])
async def cuadrado(ctx, var1):
    response = int(var1) ** int(2)
    statement = ("El numero " + str(var1) + " al cuadrado es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Cubo
@bot.command(aliases=['e3', 'E3'])
async def cubo(ctx, var1):
    response = int(var1) ** int(3)
    statement = ("El numero " + str(var1) + " al cubo es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)


# Dividir
@bot.command(aliases=['D', 'd', 'Division'])
async def division(ctx, var1,var2):
    div = int(var1)/int(var2)
    rest = int(var1)%int(var2)
    statement = ("La división de " + str(var1) + "/" + str(var2) + " es igual a: "+"{:.2f}".format(int(div))+"\nY tiene un residuo de: "+ "{:.2f}".format(int(rest)))
    await ctx.send(statement)


bot.run(TOKEN)

import os
import discord
import youtube_dl
import urllib.request
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('KEY_YOUTUBE');

bot = commands.Bot(command_prefix='!') #Prefijo del bot

@bot.command(name='ayuda') #Indice de comandos
async def help(ctx):
    response = "Hola mi Nombre es Chad Bot, soy la creación de over, por ahora no puedo hacer muchas cosas pero trato de hacer mi mejor esfuerzo. " \
               "\n\nLa lista de comandos son los siguientes: \n   !mlp  \n   !Zokram  \n   !Skmlla  \n   !Yossef  \n   !Over  \n   !ctm " \
               "\n\nEn caso de hacer una operción debes poner el prefijo inicial y luego los dos numeros con uan separacion de espacio entre ellos. " \
               "\nPuedo calcular con: \n   !S sumar \n   !R restar \n   !M multiplicar \n   !E Exponencial \n   !E2 Cuadrado \n   !E3 Cubo \n   !D dividir " \
               "\n\nRecuerda siempre usar mi prefijo ! para hablarme en cualquier comando."
    await ctx.send(response)

@bot.command(name='mlp')
async def mlp(ctx):
    response = "@AxwellG NGE#4759 está bien pendejo"
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
    response = "Chinga tu madre mami chan"
    await ctx.send(response)

#Matemáticas

@bot.command(name='S') #Suma
async def sumar(ctx, var1,var2):
    response = int(var1)+int(var2)
    statement = ("La suma de "+str(var1)+"+"+str(var2)+" es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='R') #Resta
async def restar(ctx, var1,var2):
    response = int(var1)-int(var2)
    statement = ("La resta de " + str(var1) + "-" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='M') #Multiplicar
async def multiplicar(ctx, var1,var2):
    response = int(var1)*int(var2)
    statement = ("La multiplicacion de " + str(var1) + "*" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='E') #Exponencial
async def exp(ctx, var1,var2):
    response = int(var1)**int(var2)
    statement = ("El numero " + str(var1) + "^" + str(var2) + " es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='E2') #Cuadrado
async def cuadrado(ctx, var1):
    response = int(var1) ** int(2)
    statement = ("El numero " + str(var1) + " al cuadrado es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='E3') #Cubo
async def cubo(ctx, var1):
    response = int(var1) ** int(3)
    statement = ("El numero " + str(var1) + " al cubo es igual a: "+"{:,d}".format(int(response)))
    await ctx.send(statement)

@bot.command(name='D') #Dividir
async def division(ctx, var1,var2):
    div = int(var1)/int(var2)
    cocient = int(var1)//int(var2)
    rest = int(var1)%int(var2)
    statement = ("La división de " + str(var1) + "/" + str(var2) + " es igual a: "+"{:.2f}".format(int(div))+"\nCon un cociente de: "+"{:.1f}".format(int(cocient))+"\nY un residuo de: "+ "{:.2f}".format(int(rest)))
    await ctx.send(statement)

#Discord

@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Espera que la canción actual acabe o usa el comando 'Stop'")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpefExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Ni si quiera estoy en el canal de voz para que me corras")

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("No hay ningún audio que pueda pausar actualmente")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("El audio no está pausado man")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

bot.run(TOKEN)

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('KEY_YOUTUBE');

bot = commands.Bot(command_prefix='!') #Prefijo del bot


@bot.command(name='mlp')
async def mlp(ctx):
    response = "@AxwellG NGE#4759 está bien pendejo"
    await ctx.send(response)

@bot.command(name='Zokram')
async def mlp(ctx):
    response = "Vamos Zokram habla como loli"
    await ctx.send(response)

@bot.command(name='Skmlla')
async def mlp(ctx):
    response = "Camara Saquen el WildRift"
    await ctx.send(response)

@bot.command(name='Yossef')
async def mlp(ctx):
    response = "Callese viejo ridiculo"
    await ctx.send(response)

@bot.command(name='Over')
async def mlp(ctx):
    response = "Te quiero papi"
    await ctx.send(response)

@bot.command(name='ctm')
async def mlp(ctx):
    response = "Chinga tu madre mami chan"
    await ctx.send(response)

@bot.command(name='S') #Suma
async def sumar(ctx, var1,var2):
    response = int(var1)+int(var2)
    statement = ("La suma de "+str(var1)+"+"+str(var2)+" es igual a: ")
    await ctx.send(statement)
    await ctx.send(response)

@bot.command(name='R')
async def restar(ctx, var1,var2):
    response = int(var1)-int(var2)
    await ctx.send(response)

@bot.command(name='M')
async def multiplicar(ctx, var1,var2):
    response = int(var1)*int(var2)
    await ctx.send(response)

@bot.command(name='D')
async def division(ctx, var1,var2):
    response = int(var1)/int(var2)
    await ctx.send(response)

bot.run(TOKEN)

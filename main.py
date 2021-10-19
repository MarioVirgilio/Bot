import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')  # Prefijo del bot

f = open("rules.txt","r")
rules = f.readlines()

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(aliases=['rule'])
async def regla(ctx,*, number):
    await ctx.send(rules[int(number) - 1])

@bot.command(aliases=['rules'])
async def reglas(ctx):
    response =":one: Mandar pack obligatorio para entrar en confianza. " \
              "\n:two: Usar NGE en el Nombre tanto en DL como en Discord gei el que no lo use." \
              "\n:three: Mandar a chingar a su madre a U7 y al zeroTG " \
              "\n:four: Evitar salirse del grupo general, de lo contrario serán acreedores a una Sanción."
    await ctx.send(response)

@bot.command(aliases=['c','clean','b','borra'])
@commands.has_permissions(manage_messages=True)
async def borrar(ctx,amount=2):
    await ctx.channel.purge(limit=amount)

@bot.command(aliases=['k','kick'])
@commands.has_permissions(kick_members=True)
async def expulsar(ctx,member: discord.Member,*,reason= "Sin ninguna razón en particular"):
    await member.send("Regresa a fornite fan de la CQ te kickeamos porque: "+reason)
    await member.kick(reason=reason)

@bot.command(aliases=['banamex'])
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,*,reason= "Sin ninguna razón en particular"):
    await member.send(member.name + "Regresa a fornite fan de la CQ te baneamos porque: "+reason)
    await member.ban(reason=reason)

bot.run(TOKEN)

import discord
import os
import json

from discord.ext import commands, tasks
from itertools import cycle
from dotenv import load_dotenv


# Cogs
from main_cog import main_cog
from math_cog import math_cog
from other_cog import other_cog

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
filtered_words = ["Laxus", "laxus", "PKM", "pkm"]
status = cycle(['With ur mom', 'Gay el que lo lea', 'Sus', 'DB super es para pendejos'])

#Obtiene el prefijo asignado
def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        return prefixes[str(message.guild.id)]

# Prefijo del bot
bot = commands.Bot(command_prefix=get_prefix)

# Remover el comando de ayuda para usar el nuestro
bot.remove_command('help')


# Registro de clases
bot.add_cog(main_cog(bot))
bot.add_cog(math_cog(bot))
bot.add_cog(other_cog(bot))


# Inicio
@bot.event
async def on_ready():
    change_status.start()
    print("Bot is ready")


# Estatus
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


# Agregar ID al unirse a discord
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


# Borrar ID de canal al salirse
@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


# Cambiar Prefijo
@bot.command()
@commands.has_permissions(kick_members=True)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'El prefijo cambio a: "{prefix}"')

bot.run(TOKEN)
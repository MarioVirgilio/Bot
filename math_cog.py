import discord
import os

from discord.ext import commands


#Responsable de todo los comandos matemáticos
class math_cog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot


    # Suma
    @commands.command(name="Sumar", aliases=['S', 's', 'SUMAR', 'sumar'], help="Suma 2 cantidades")
    async def sumar(self, ctx, var1, var2):
        response = float(var1) + float(var2)
        statement = ("La suma de " + str(var1) + " + " + str(var2) + " es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)


    # Resta
    @commands.command(name="Restar", aliases=['R', 'r', 'RESTAR', 'restar'], help="Resta 2 cantidades")
    async def restar(self, ctx, var1, var2):
        response = float(var1) - float(var2)
        statement = ("La resta de " + str(var1) + "-" + str(var2) +  " es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)


    # Multiplicar
    @commands.command(name="Multiplicar", aliases=['X', 'x', 'MULTIPLICAR', 'multiplicar'], help="Multiplica 2 cantidades")
    async def multiplicar(self, ctx, var1, var2):
        response = float(var1) * float(var2)
        statement = ("La multiplicacion de " + str(var1) + " * " + str(var2) + " es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)


    # Dividir
    @commands.command(name="Dividir", aliases=['D', 'd', 'DIVIDIR', 'dividir'], help="Divide 2 cantidades")
    async def dividir(self, ctx, var1, var2):
        div = float(var1) / float(var2)
        rest = float(var1) % float(var2)
        statement = ("La división de " + str(var1) + "/" + str(var2) + " es igual a: " + "{:,.2f}".format(float(div)) +  "\nTiene un residuo de: " + "{:,.2f}".format(float(rest)))
        await ctx.send(statement)


    # Exponencial
    @commands.command(name="Exponencial", aliases=['E', 'e', 'exponencial', 'Exp', 'exp'], help="Exponencia un número en una cantidad deseada")
    async def exp(self, ctx, var1, var2):
        response = float(var1)**float(var2)
        statement = ("El numero " + str(var1) + "^" + str(var2) + " es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)


    # Cuadrado
    @commands.command(name="Cuadrado", aliases=['e2', 'E2', 'CUADRADO', 'cuadrado'], help="Exponencia al cuadrado un numero")
    async def cuadrado(self, ctx, var1):
        response = float(var1)**float(2)
        statement = ("El numero " + str(var1) + " al cuadrado es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)


    # Cubo
    @commands.command(name="Cubo", aliases=['e3', 'E3', 'CUBO', 'cubo'], help="Exponencia al cubo un numero")
    async def cubo(self, ctx, var1):
        response = float(var1)**float(3)
        statement = ("El numero " + str(var1) + " al cubo es igual a: " + "{:,.2f}".format(float(response)))
        await ctx.send(statement)
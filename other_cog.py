import discord
import random
from discord.ext import commands


cartas = [
    'https://static.wikia.nocookie.net/yugiohenespanol/images/d/dd/Foto_n%C3%BAmero_39_utop%C3%ADa.jpg/revision/latest?cb=20120122053915&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/58/Foto_mago_oscuro.jpg/revision/latest?cb=20120121043211&path-prefix=es',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/5/55/Foto_h%C3%A9roe_elemental_neos.jpg/revision/latest?cb=20120202055949&path-prefix=es',
    'https://static.zerochan.net/Odd-Eyes.Pendulum.Dragon.full.3210952.jpg',
    'https://static.wikia.nocookie.net/yugiohenespanol/images/b/b6/Foto_decodificador_hablador.jpg/revision/latest?cb=20170321191013&path-prefix=es'
]


class other_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
#Otros


    # Golpe
    @commands.command(name='Golpe', aliases=['punch', 'Punch', 'golpe'])
    async def golpe(self, ctx, *, member: discord.Member):
        listGifs = [
            'https://c.tenor.com/DMWqIb2Rdp4AAAAi/bonk-cheems.gif',
            'https://c.tenor.com/cqnZ1RW_XjsAAAAC/horny-bonk.gif',
            'https://c.tenor.com/O0XLzUO24X4AAAAC/sape-golpear.gif',
            'https://c.tenor.com/JEvWuCTiIZcAAAAC/sape-un.gif',
            'https://c.tenor.com/PTONt_7DUTgAAAAC/batman-slap-robin.gif',
            'https://c.tenor.com/gFqmPEMWqEQAAAAC/the-simpsons-homer-simpson.gif',
            'https://c.tenor.com/XhdHGRof6WEAAAAC/anime-ataque-golpe-en-la-pared.gif'
        ]

        punch_embed = discord.Embed( title='  ', description= f"**{member}** te envía un madrazo el usuario **{ctx.author}** por retard", color=discord.Color.blue())
        punch_embed.set_image(url=random.choice(listGifs))
        await ctx.send(embed=punch_embed)


    # Apreton
    @commands.command(name='Apreton', aliases=['handshake', 'Handshake', 'apreton'])
    async def apreton(self, ctx, *, member: discord.Member):
          listGifs = [
              'https://c.tenor.com/9t3luBDOyHEAAAAC/the-simpsons-simpson.gif',
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

          hand_embed = discord.Embed( title='  ', description=f"**{member}** hombre de cultura **{ctx.author}**", color=discord.Color.blue())
          hand_embed.set_image(url=random.choice(listGifs))
          await ctx.send(embed=hand_embed)
          

    # Carta al azar
    @commands.command(name='Carta', aliases=['card', 'Card'])
    async def carta(self, ctx):
        embed = discord.Embed(color=discord.Color.red())
        random_link = random.choice(cartas)
        embed.set_image(url=random_link)
        await ctx.send(embed=embed)


    # Azar
    @commands.command(name='Azar', aliases=['azar'])
    async def bola8(self, ctx, *, question):
        response = [
            'En mi opinión, sí', 'Es cierto', 'Es decididamente así',
            'Probablemente', 'Buen pronóstico', 'Todo apunta a que sí', 'Sin duda',
            'Sí', 'Sí - definitivamente', 'Debes confiar en ello',
            'Respuesta vaga, vuelve a intentarlo', 'Pregunta en otro momento',
            'Será mejor que no te lo diga ahora', 'No puedo predecirlo ahora',
            'Concéntrate y vuelve a preguntar', 'Puede ser', 'No cuentes con ello',
            'Mi respuesta es no', 'Mis fuentes me dicen que no',
            'Las perspectivas no son buenas', 'Muy dudoso'
        ]

        _8ball_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        _8ball_embed.add_field(name="Comando Azar | :8ball:", value= f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}")
        await ctx.send(embed=_8ball_embed)


    # Moneda
    @commands.command(name='Moneda', aliases=['toss', 'Toss', 'moneda'])
    async def moneda(self, ctx):
        response = ['Cara', 'Cruz']
        moneda_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        moneda_embed.add_field(name="Comando Moneda | :coin:", value=f"{random.choice(response)}")
        await ctx.send(embed=moneda_embed)


    # Dado
    @commands.command(name='Dado6', aliases=['roll6', 'dado6', 'Roll6'])
    async def dado6(self, ctx):
        response = [':one:', ':two:', ':three:', ':four:', ':five:', ':six:']
        dado_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        dado_embed.add_field(name="Comando Dado | :ice_cube:", value=f"{random.choice(response)}")
        await ctx.send(embed=dado_embed)


    # Dos dados de seis caras
    @commands.command(name='DobleDado', aliases=['2roll6', '2dado6', 'dobledado'])
    async def dobledado(self, ctx):
        response = [
            ':one:-:one:', ':one:-:two:', ':one:-:three:', ':one:-:four:',
            ':one:-:five:', ':one:-:six:', ':two:-:one:', ':two:-:two:',
            ':two:-:three:', ':two:-:four:', ':two:-:five:', ':two:-:six:',
            ':three:-:one:', ':three:-:two:', ':three:-:three:', ':three:-:four:',
            ':three:-:five:', ':three:-:six:', ':four:-:one:', ':four:-:two:',
            ':four:-:three:', ':four:-:four:', ':four:-:five:', ':four:-:six:',
            ':five:-:one:', ':five:-:two:', ':five:-:three:', ':five:-:four:',
            ':five:-:five:', ':five:-:six:', ':six:-:one:', ':six:-:two:',
            ':six:-:three:', ':six:-:four:', ':six:-:five:', ':six:-:six:'
        ]

        dado_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        dado_embed.add_field(name="Comando Dado | :ice_cube:", value=f"{random.choice(response)}")
        await ctx.send(embed=dado_embed)


    # Rate/Calificar
    @commands.command(name='Calificar', aliases=['rate', 'Rate', 'calificar'])
    async def calificar(self, ctx, *, question):
        response = [
            '0/10', '1/10', '2/10', '3/10', '4/10', '5/10', '6/10', '7/10', '8/10',
            '9/10', '10/10', '9/11 bruh'
        ]

        rate_embed = discord.Embed(title='  ', description=f"  ", color=discord.Color.blue())
        rate_embed.add_field( name="Comando Rate | :100:", value= f"**Pregunta:** {question}\n**Respuesta:** {random.choice(response)}")
        await ctx.send(embed=rate_embed)


    @commands.command(name='Ctm', aliases=['ctm'])
    async def ctm(self, ctx):
       await ctx.send("ctm mamón <:Fuck:765783371167039548>")
  

    @commands.command(name='Mlp', aliases=['mlp'])
    async def mlp(self, ctx):
        response = "@AxwellG NGE#4759 está bien pendejo :100:"
        await ctx.send(response)


    @commands.command(name='Zokram', aliases=['zokram'])
    async def zokram(self, ctx):
        response = "Vamos Zokram habla como loli"
        await ctx.send(response)


    @commands.command(name='Skmlla', aliases=['skmlla'])
    async def skmlla(self, ctx):
        response = "Camara Saquen el WildRift"
        await ctx.send(response)


    @commands.command(name='Yossef', aliases=['yossef'])
    async def yossef(self, ctx):
        response = "Callese viejo ridiculo"
        await ctx.send(response)


    @commands.command(aliases=['Over'])
    async def over(self, ctx):
        response = "Te quiero papi <:mmmm:765440193217822742>"
        await ctx.send(response)
  
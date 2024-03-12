import discord, random, os
from bot_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def mem(ctx):

    image = random.choice(os.listdir("images"))

    with open(f'images/{image}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def que_limpio(ctx):
    frases = ["Ve a limpiar una playa","Limpia basura de un parque","Puedes limpiar la basura de la calle"]
    frase = random.choice(frases)
    await ctx.send(frase)

@bot.command()
async def que_ayudo(ctx):
    frases = ["Puedes plantar arboles","Puedes ahorrar agua","Recicla/reutiliza plasticos"]
    frase = random.choice(frases)
    await ctx.send(frase)

@bot.command()
async def que_hago(ctx):
    frases = ["Puedes hacer regaderas de pantas con botellas", "No usar muchas cosas de plastico", "usar cosas ecológicas"]
    frase = random.choice(frases)
    await ctx.send(frase)
    




bot.run("TOKEN")

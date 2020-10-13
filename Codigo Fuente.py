#Ready Python Bot
import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='.', description="Py Bot")

#para dar bienvenida
@bot.event
async def on_member_join(member):
    print(f'{"member"} bienvenido al server!')
    
@bot.event
async def on_member_remove(member):
    print(f'{"member"} Se fue del server F!')

#comando personalizado
@bot.command()
async def repo(ctx):
    await ctx.send('https://github.com/LemonCod3')



#comando basico
@bot.command()
async def ping(ctx):
        await ctx.send('pong')



#comando de calculadora
@bot.command()
async def multiplica(ctx, numeroUNO: int, numeroDOS: int):
    await ctx.send(numeroUNO * numeroDOS)

@bot.command()
async def suma(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def divide(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne / numTwo)

@bot.command()
async def resta(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne - numTwo)



#mensaje de comandos
@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title="Mis Comandos", description="comandos del LemonBot (py)", timestamp=datetime.datetime.utcnow(), color=discord.Color.Yellow()) #puedes poner cualquier color pero en ingles
    embed.add_field(name="Clear", value="borrar mensajes")
    embed.add_field(name="calculadora", value=".suma .resta etc...")
    embed.add_field(name="avatar", value="imagen del usuario")
    embed.add_field(name="serverinfo", value="informacion del server")
    embed.add_field(name="Prefix", value=".")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="aqui va una foto del bot")

    await ctx.send(embed=embed)
    


#comando clear    
@bot.command(pass_context=True)
async def clear(ctx, amount=None):
 await ctx.channel.purge(limit=int(amount)+1)
 await ctx.send(str(amount)+" Mensajes Borrados :D !")



#informacion del server
@bot.command()
async def serverinfo(ctx):
    def filtro_usuarios(miembros): #Hacemos el filtro para los usuarios
        
        if miembros.bot == False:
            return True

    #-

    def filtro_bots(miembros): # Este sera el filtro para los bots
        
        if miembros.bot == True:
            return True

    #-

    embed = discord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(),
    color=discord.Color.green()) # el color no se como ponerlo en random asi que lo puse verde

    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.add_field(name="Nombre", value=f"{ctx.guild.name}")
    embed.add_field(name="ID", value=f"{ctx.guild.id}")
    embed.add_field(name="Región", value=f"{ctx.guild.region}")
    embed.add_field(name="Miembros totales", value=f"{len(ctx.guild.members)}")
    embed.add_field(name="Bots", value=f"{len(list(filter(filtro_bots, ctx.guild.members)))}")
    embed.add_field(name="Usuarios", value=f"{len(list(filter(filtro_usuarios, ctx.guild.members)))}")
    embed.add_field(name="Roles", value=f"{len(ctx.guild.roles)}")
    embed.add_field(name="Canales", value=f"{len(ctx.guild.channels)}")
    embed.add_field(name="Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Fecha de creación", value=f"{ctx.guild.created_at}")

    await ctx.send(embed=embed) #enviamos el embed

  

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Memes", url="https://www.twitch.tv/elded"))
    print('Andamos Ready !!!')



#para el avatar
@bot.command()
async def avatar(ctx):
    await ctx.send(f"{ctx.author} este es tu avatar {ctx.author.avatar_url}")



#ban
@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.send("¡El Mod {} ha baneado al usuario {}!".format(ctx.author.name, member.name))



#kick
@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.send("¡El usuario {} ha kickeado al usuario {}!".format(ctx.author.name, member.name))



#nuevo comando,GA
@client.command()
async def prueba(texto : str):
    print('Comando de prueba ejecutado, texto recibido: ' + texto)
    await client.say(ctx.message.author + ':ok_hand:')



#abajo en las comillas va el token del bot
bot.run('0p3n sourc3')
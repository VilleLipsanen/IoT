import discord
from discord.ext import commands
import urllib.request
import urllib.parse
import json


TOKEN = 'token here'

url = "http://api.apixu.com/v1/current.json?key=b60fa3731a3e4a3d8a4103415191402&q=Oulu"

response = urllib.request.urlopen(url)
wjson = response.read()
wjdata = json.loads(wjson)

#tempc = response, current,temp_c
saa = wjdata['current']['temp_c']
tuuli = wjdata['current']['wind_kph']
saatila = wjdata['current']['condition']['text']
tuntuu = wjdata['current']['feelslike_c']

ilma = "saa: {} tuuli: {} ilma: {} tuntuu iholla: {}".format(saa, tuuli, saatila, tuntuu)

print (wjdata['current']['temp_c'])
print (wjdata['current']['wind_kph'])

description = '''Samu-Simulaattori'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def Terve():
    
    await bot.say("No terve")
@bot.command()
async def Paljo_on_lamminta():
await bot.say(saa)

@bot.command()
async def Ilma():
await bot.say(ilma)

@bot.command()
async def add(left : int, right : int):
    
    await bot.say(left + right)

bot.run(TOKEN)
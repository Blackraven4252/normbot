import discord
import os
from random import choice
from discord.ext import commands
import random
from discord import app_commands
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)
MY_GUILD = discord.Object(id=0)  # replace with your guild id
funcional = ["$mem", "hello", "$animalmem", "помощь"]
@bot.command()
async def mem(ctx):
    image = choice(os.listdir('images'))
    with open(f'images/{image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
      # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def animalmem(ctx):
    animage = choice(os.listdir('animages'))
    with open(f'animages/{animage}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
      # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run("ТОКЕН")

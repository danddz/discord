import random

import discord
from discord.ext import commands, tasks
from discord.ui import Button, View

import files_draft.Pokemons as Pokemons
from files_draft.Buttons import ReadyButton, ReadyButton_eu

from files_wheel_fortune.categories import categories
from files_wheel_fortune.phrases import single_phrases, double_phrases

import files_rps.rps_settings as rps_settings
from files_rps.Buttons import RPSButton

import database.database as database

token_main = 'TOKEN HERE'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print('ready')

@bot.command(name='драфт', help='Командный выбор покемонов с системой банов. Пример !драфт @gIDOHXypqh4y#7327')
async def draft(ctx, *, message=''):
    user_1 = str(ctx.message.author.mention)
    user_2 = message[message.find('<@'):message.find('>') + 1]
    if user_2 != '':
        msg = f'Драфт между командами {user_1} и {user_2}.\nКапитан {user_1} выбирает КОЛИЧЕСТВО банов.'
        view = View(timeout=60*60)
        for i in Pokemons.list_0:
            view.add_item(ReadyButton(i, msg, 0, [user_1, user_2], [], [[], []], [], 0, 0, True))

        message = await ctx.send(msg, view=view)

@bot.command(name='колесо', help='Случайный выбор покемонов с одинаковыми признаками. Пример !колесо или !колесо @gIDOHXypqh4y#7327')
async def wheel_fortune(ctx, *, message=''):
    type_rnd = random.choice(list(categories.keys()))
    response = type_rnd + ': ' + ', '.join(categories[type_rnd])

    chance_of_azumarill = 5
    additional_text = str()

    user_1 = str(ctx.message.author.mention)
    user_2 = message[message.find('<@'):message.find('>') + 1]

    if user_2 != '':
        phrase = random.choice(double_phrases).format(user_1=user_1, user_2=user_2)

        if random.randint(0, 100) <= chance_of_azumarill:
            additional_text = 'P.S. Вам придётся совершить петушиный поступок - обязательный пик Талонфлейма в обоих командах.'

        msg = f'{phrase}\n{response}.\n{additional_text}'
    else:
        phrase = random.choice(single_phrases).format(user_1=user_1)

        if random.randint(0, 100) <= chance_of_azumarill:
            additional_text = 'P.S. Вам придётся совершить петушиный поступок - обязательный пик Талонфлейма.'

        msg = f'{phrase}\n{response}.\n{additional_text}'

    message = await ctx.send(msg)

@bot.command(name='draft', help='Team selection of Pokemon with a system of bans. Example !d?raft @gIDOHXypqh4y#7327')
async def draft(ctx, *, message=''):
    user_1 = str(ctx.message.author.mention)
    user_2 = message[message.find('<@'):message.find('>') + 1]
    if user_2 != '':
        msg = f'Draft between captains {user_1} и {user_2}.\nCaptain {user_1} chose NUMBER of bans.'
        view = View(timeout=60*60)
        for i in Pokemons.list_0:
            view.add_item(ReadyButton_eu(i, msg, 0, [user_1, user_2], [], [[], []], [], 0, 0, True))

        message = await ctx.send(msg, view=view)

@bot.command(name='кнб', help='Кнб на лад покемонов')
async def rps(ctx, *, message=''):
    user_1 = str(ctx.message.author.mention)
    user_2 = message[message.find('<@'):message.find('>') + 1][:-1][2:]

    msg = f'Создатель {user_1}.\nВыберите тип и дождитесь противника.\n'
    if user_2 != '':
        msg = f'Создатель {user_1}.\nВыберите тип и дождитесь <@{user_2}>.\n'

    view = View(timeout=15*60)
    for i in rps_settings.list_1:
        view.add_item(RPSButton(i, msg, {}, '', user_1[:-1][2:], user_2, 0))

    message = await ctx.send(msg, view=view)

@bot.command(name='топ', help='Топ игроков кнб')
async def top(ctx, *, message=''):
    user_1 = int(ctx.message.author.id)
    msg = database.get_top_rps(user_1)
    message = await ctx.send(msg)

# @bot.command(name='qqq', help='Team selection of Pokemon with a system of bans. Example !draft @gIDOHXypqh4y#7327')
# async def draft(ctx, *, message=''):
#     print(bot.guilds)


bot.run(token_main)

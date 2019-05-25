#-*-coding:utf-8-*-
"""
回声机器人

"""

import asyncio
import aiohttp
import logging
import ssl

import weather
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN

#PROXY_URL = 'http://127.0.0.1:8001';

# 配置日志
logging.basicConfig(level=logging.INFO)

# 初始化机器人和调度器

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    """
    这个函数将会被回调，当客户端输入'/start'或者'/help'命令时
    """
    await message.reply("欢迎来到jacklov3的垃圾机器人\n,请问有什么可以帮助您的吗？")

@dp.message_handler(commands=['weather'])
async def re_weather(message: types.Message):
        if len(message.text)==8:
            await message.reply('你的用法好像有问题，应该是/weather 北京市')
        else:
            await message.reply(weather.get_weather(message.text.split()[1]))


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, '轻，人家理解不了您的请求呢😄 \t'+message.text)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

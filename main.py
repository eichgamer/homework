#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import TeleBot

from client import BotClient

telegram_bot = TeleBot("354252761:AAH92i35ZjkO56emVjEQvmY67YCRUnWWb8w")


@telegram_bot.message_handler(commands=["start"])
def send_book_name(message):
    client = BotClient()
    body = client.get_http_response()
    book_name = client.get_book_name(body)
    telegram_bot.reply_to(message, book_name)


telegram_bot.polling()

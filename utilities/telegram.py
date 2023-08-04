from pyrogram import Client
import os
import json
import time
with open("helpers/text.json","r",encoding="utf-8") as text_data:
    text_data = json.load(text_data)

def BotExist() -> bool|str:
    try:
        with open("cache/bot.txt", "r", encoding="utf-8") as file_data:
            bot_token = file_data.read()

    except Exception:
        return False
    
    return bot_token

def BotWrite(bot_token:str) -> None:
    with open("cache/bot.txt", "w", encoding="utf-8") as file_data:
        file_data.write(bot_token)

def BotRemove() -> None:
    os.remove("cache/bot.txt")

def AppendData(msg_id:str, data:str) -> None:
    try:
        with open("result.json","+r", encoding="utf-8") as file_data:
            json_data = json.load(file_data)
            json_data[msg_id] = data

    except FileNotFoundError:
        with open("result.json", "w", encoding="utf-8") as file_data:
            file_data.write("{}")
            json_data = {}

    with open("result.json", "w", encoding="utf-8") as file_data:
        json.dump(json_data, file_data, indent=4)

class Telegram:
    def __init__(self, bot_token:str) -> None:
        self.bot_token = bot_token
    
    def start(self):
        self.bot = Client(name=self.bot_token, bot_token=self.bot_token, api_id=12704312, api_hash="b5840c5334ac3694b2af0601db6d71f7", workdir="cache/").start()

    def save(self, message:object):
        if message.text:
            AppendData(message.id, message.text)

            return True
        
        else:
            if message.caption != None:
                AppendData(message.id, message.caption)
                return True

            return False

    def download(self, message:object):
        def prog_func(current, total): 
            print(f'Message ID [{message.id}] - {float(current) / 1000.0}/{float(total) / 1000.0} KB')
        message.download(progress=prog_func, block=True, progress_args=())
    
    def get_message(self, channel_id:str, message_id:int):
        return self.bot.get_messages(channel_id, message_id)
        

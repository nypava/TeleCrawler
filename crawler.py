from utilities.telegram import Telegram, BotExist, BotWrite, BotRemove
from utilities.terminal import clear, print_color, banner
import os
import requests
import json
import time

with open("helpers/text.json","r",encoding="utf-8") as text_data:
    text_data = json.load(text_data)


class Main:

    def InternetCheck(self):
        clear()
        check_text = text_data["internet_check"]
        print(check_text)

        try:
            requests.get("https://motherfuckingwebsite.com") # This is not what you are thinking about
            clear()

        except Exception:
            clear()
            fail_text = text_data["internet_fail"]
            print_color(fail_text, "RED")
            return
        
        self.GetBotToken()

    def GetBotToken(self):
        clear()
        banner()

        if BotExist() != False:
            bot_old_text = text_data["bot_old_input"]
            bot_response = input(bot_old_text)

            if bot_response.lower() == "y":
                try:
                    self.bot = Telegram(BotExist())
                    self.bot.start()

                except Exception:
                    bot_fail_text = text_data["bot_fail"].format(e)
                    print_color(bot_fail_text, "RED")
                    time.sleep(4)
                    BotRemove()
                    self.GetBotToken()

                    return
                
                self.MainChoice()

                return
                    
        bot_new_text = text_data["bot_new_input"]
        bot_token = input(bot_new_text)

        try:
            self.bot = Telegram(bot_token)
            self.bot.start()
            
        except Exception as e:
            bot_fail_text = text_data["bot_fail"].format(e)
            print_color(bot_fail_text, "RED")
            time.sleep(4)
            self.GetBotToken()

            return

        BotWrite(bot_token)
        self.MainChoice()
    
    def MainChoice(self): 
        clear()
        banner()
        main_prompt_text = text_data["main_prompt"]
        main_choice = input(main_prompt_text)

        if main_choice.strip() == "1":
            self.Crawler()

        elif main_choice.strip() == "2":
            self.Downloader()

        elif main_choice.strip() == "3":
            os._exit(0)

        else:   
            main_fail_text = text_data["main_fail"]
            print_color(main_fail_text, "RED")
            time.sleep(4)
            clear()
            self.MainChoice()

    def IntialUrl(self):

        try:
            intial_msg_text = text_data["intial_msg"]
            intial_url = input(intial_msg_text)
            channel_id, msg_id = intial_url.split("/")[-2:]
            
            return channel_id, msg_id 
        
        except Exception: 
            invalid_url_text = text_data["invalid_url"]
            print_color(invalid_url_text, "RED")
            time.sleep(4)

        self.CurrentChoose()

    def FinalUrl(self):

        try:
            intial_msg_text = text_data["final_msg"]
            intial_url = input(intial_msg_text)
            channel_id, msg_id = intial_url.split("/")[-2:]

            return channel_id, msg_id 
        
        except Exception:
            invalid_url_text = text_data["invalid_url"]
            print_color(invalid_url_text, "RED")
            time.sleep(4)

        eval(self.CurrentChoose+"()")
    
    def Crawler(self):
        
        self.CurrentChoose = "self.Crawler()"
        clear()
        banner()
        intial_cid, intial_mid = self.IntialUrl()
        clear()
        banner()
        final_cid, final_mid = self.FinalUrl()

        if intial_cid != final_cid:
            channel_fail_url = text_data["channel_fail"]
            print_color(channel_fail_url, "RED")
            time.sleep(4)
            self.Crawler()
        
        clear()
        save_log_text = text_data["save_log"]
        print(save_log_text)

        for msg_id in range(int(intial_mid), int(final_mid) + 1):
            message = self.bot.get_message(intial_cid, msg_id)
            saved = self.bot.save(message)

            if saved == True:
                saved_notify_text = text_data["saved_nofiy"].format(msg_id)
                print(saved_notify_text)
          
        clear()
        self.MainChoice()

    def Downloader(self):
        self.CurrentChoose = "self.Downloader()"
        clear()
        banner()
        intial_cid, intial_mid = self.IntialUrl()
        clear()
        banner()
        final_cid, final_mid = self.FinalUrl()

        if intial_cid != final_cid:
            channel_fail_url = text_data["channel_fail"]
            print_color(channel_fail_url, "RED")
            time.sleep(4)
            self.Downloader()
        
        clear()
        download_log_text = text_data["save_log"]
        print(download_log_text)

        for msg_id in range(int(intial_mid), int(final_mid) + 1):
            message = self.bot.get_message(intial_cid, msg_id)
            self.bot.download(message)

        clear()
        self.MainChoice()

    def run(self):
        self.InternetCheck()

if __name__ == "__main__":
    Main().run()


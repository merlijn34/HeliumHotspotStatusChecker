# Imports
import requests
import os
from dotenv import load_dotenv

# Credentials
load_dotenv('.env')

api_url = 'https://api.helium.io/v1/'
hotspot_address = os.getenv('HOTSPOT_ADDRESS');

def telegram_bot_sendtext(bot_message):
    
    bot_token = os.getenv('BOT_TOKEN');
    bot_chatID = os.getenv('BOT_CHAT_ID');
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    # return response.json()
    

test = telegram_bot_sendtext("Test message")
# print(test)





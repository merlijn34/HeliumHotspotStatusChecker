# Imports
import requests
import os
from dotenv import load_dotenv
import json

import time
import schedule

# Credentials
load_dotenv('.env')

#API info
api_url = 'https://api.helium.io/v1/'
hotspot_address = os.getenv('HOTSPOT_ADDRESS');

hotspots = ['tangy-blood-lion', 'clumsy-syrup-rooster', 'creamy-tangerine-jaguar']

# py:function:: hotspot_by_name(hotspot)
#    makes a call to the helium API per hotspot and returns the hotspot details and checks if the hotspot is online and in sync
#    :param str hotspot: Name of the hotspot
def hotspot_by_name(hotspot):

	#call the API
	response = requests.get(api_url + 'hotspots/' + 'name/' + hotspot)

	# if we get a bad respsonse timeout and run the job again 
	if (response.status_code != 200):
		time.sleep(3600) #1 uur
		schedule.every(10).minutes.do(job)
		telegram_bot_sendtext('we got a timeout from the API. We start again in t -60s')
	else :
		#TODO filter when value is no good or error
		#get the value's from the response
		hotspot_name = response.json()['data'][0]['name']
		hotspot_status = response.json()['data'][0]['status']['online']
		hotspot_block_height = response.json()['data'][0]['status']['height']
		blockchain_height = response.json()['data'][0]['block']

		# print(json.dumps(response_json, indent=4))
		# print(hotspot_block_height, blockchain_height, hotspot_status)

		#check if the hotspot is in sync with the blockchain 
		#TODO when is a hotspot out of sync? after how many block difference
		hotspot_sync = sync_status(blockchain_height, hotspot_block_height)


		# If the hotspot is offline send a message with info
		if str(hotspot_status) == 'offline':
			my_message = '❗️❗️❗️Hotspot offline❗️❗️❗️' + '\n' + 'hotspot: ' + str(hotspot_name) + '\n' + 'STATUS: ' + str(hotspot_status) + '\n' + 'sync status: ' + str(hotspot_sync)
			telegram_bot_sendtext(my_message)
	
# py:function:: sync_status(blockchain_height, hotspot_block_height)
#    makes a call to the helium API per hotspot and returns the hotspot details and checks if the hotspot is online and in sync
#    :param str blockchain_height: height of the blockchain
#    :param str hotspot_block_height: height of the hotspot blockchain
def sync_status(blockchain_height, hotspot_block_height):
	if blockchain_height == hotspot_block_height:
		return 'hotspot is synced'
	else:
		gap = blockchain_height - hotspot_block_height
		return 'hotspot is not synced, gap is: ' + str(gap)


# py:function:: telegram_bot_sendtext(bot_message)
#    Send a message via telegram
#    :param str bot_message: The person sending the message
def telegram_bot_sendtext(bot_message):
	#telegram credentials
	bot_token = os.getenv('BOT_TOKEN');
	bot_chatID = os.getenv('BOT_CHAT_ID');
	#url with params
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

	response = requests.get(send_text)


#do this for all the hotspots in the hotspots array
def job():
	for hotspot in hotspots:
		test = hotspot_by_name(hotspot)


schedule.every(10).minutes.do(job)
#keep it runnin
while True:
	schedule.run_pending()
	time.sleep(1)
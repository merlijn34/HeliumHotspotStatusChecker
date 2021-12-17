# HeliumHotspotStatusChecker

## this is a script that checks the status of your helium hotspot every X minutes and sends a Telegram message when your hotspot is offline.

**Awesome! How does this work?**

1. first we set up Telegram
  - On Telegram, search @ BotFather, send him a “/start” message
  - Send another “/newbot” message, then follow the instructions to setup a name and a username
  - Your bot is now ready, be sure to save a backup of your API token, and correct, this API token is your bot_token
  - On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message
  - Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates , replace <yourtoken> with your API token, press enter and you should see something like this:

  ```json
{
  "ok": true,
  "result": [
    {
      "update_id": 945xxxxx,
      "message": {
      "message_id": 365,
      "from": {
      "id": 166xxxxxx,
      "is_bot": false,
      "first_name": "Merlijn",
      "language_code": "en"
    },
    "chat": {
      "id": 166xxxxx,
      "first_name": "Merlijn",
      "type": "private"
    },
    "date": 1639734628,
    "text": "/start",
    "entities": [
    {
    "offset": 0,
    "length": 6,
    "type": "bot_command"
    }
  ]
}
}
]
}
```
 



  - we save this bot token and bot id in a .env file in the same folder as the script. (there is a example of a .env file in the repo, remove 'example' in the name and save the file with your credentials. Don't upload these private keys anywhere!)
  
 2. We set up the script
  - On line 17 add your hotspot names to the array
  - On line 84 we can define how often we want to call the api and check our status (if we do this too often we get a lime-out from the api. if this happens we catch the timeout and wait 1 hour and start the script again)

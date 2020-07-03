# pip install fake-useragent
# pip install discord-webhook

import sys
import time
import random
import requests
from fake_useragent import UserAgent
from discord_webhook import DiscordWebhook, DiscordEmbed

starttime = time.time()
refreshtime = 30 # seconds

forward = "webhook-url"

memelist = [
	"memes",
	"dankmemes",
	"PewdiepieSubmissions"
]

def memes():
	ua = UserAgent()
	url = "https://www.reddit.com/r/" + random.choice(memelist) + "/randomrising/.json?kind=t3"

	response = requests.get(url, headers={'User-agent': ua.random})

	if response.ok:
		output = response.json()['data']['children']
		
		for child in range(25):
			data = output[child]['data']
			
			if data:
				if not data['over_18'] and not data['media']:
					send_discord_message(data)
					break
		
def send_discord_message(data):
	temp = "by " + data['author'] + " on " + data['subreddit_name_prefixed'] + "\n" + str(data['ups']) + " likes - " + str(data['num_comments']) + " comments"
	webhook = DiscordWebhook(url=forward)
	embed = DiscordEmbed(color=random.randint(0, 16777215))
	embed.set_author(name=data['title'], url='https://reddit.com' + data['permalink'], icon_url=data['thumbnail'])
	embed.set_footer(text=temp)
	embed.set_image(url=data['url'])
	webhook.add_embed(embed)
	response = webhook.execute()
	
while True:
	memes()
	time.sleep(float(refreshtime) - ((time.time() - starttime) % float(refreshtime)))

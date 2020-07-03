# pip install fake-useragent
# pip install discord-webhook

import time # Timer
import random # Color randomizer
import requests # GET method
from fake_useragent import UserAgent # Get memes
from discord_webhook import DiscordWebhook, DiscordEmbed # Send messages

starttime = time.time() # Start time
refreshtime = 30 # Seconds

# Webhook url
forward = "https://discordapp.com/api/webhooks/728382218636099604/4t9ScuBxxpFexevkLY8pzYE7En12I2v9BMv6evKib-Pfg9D_5ksvC5ha6a3ZUkzdHT49"

# Subreddits
memelist = [
	"memes",
	"dankmemes",
	"PewdiepieSubmissions"
]

# Get meme
def memes():
	ua = UserAgent() # Fake agent
	url = "https://www.reddit.com/r/" + random.choice(memelist) + "/randomrising/.json?kind=t3" # Json url
	response = requests.get(url, headers={'User-agent': ua.random}) # GET method

	if response.ok: # Connected to server
		output = response.json()['data']['children'] # Get json output
		
		for child in range(25): # Loop through each entry
			data = output[child]['data'] # Get entry
			
			if data: # Check if valid data
				if not data['over_18'] and not data['media']: # SFW and non-media content (images)
					send_discord_message(data) # Send discord message
					break # Send only one message

# Send discord message	
def send_discord_message(data):
	temp = "by " + data['author'] + " on " + data['subreddit_name_prefixed'] + "\n" + str(data['ups']) + " likes - " + str(data['num_comments']) + " comments" # Footer
	webhook = DiscordWebhook(url=forward) # Webhook url
	embed = DiscordEmbed(color=random.randint(0, 16777215)) # Side color
	embed.set_author(name=data['title'], url='https://reddit.com' + data['permalink'], icon_url=data['thumbnail']) # Title
	embed.set_footer(text=temp) # Footer text
	embed.set_image(url=data['url']) # Image
	webhook.add_embed(embed) # Merge embeds data
	response = webhook.execute() # POST method and receive output
	
# Main func
#while True:
memes() # MemeBot
#	time.sleep(float(refreshtime) - ((time.time() - starttime) % float(refreshtime))) # Timer

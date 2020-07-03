# pip install fake-useragent
# pip install discord-webhook

import os
import discord
import random # Color randomizer
import requests # GET method
from fake_useragent import UserAgent # Get memes
from discord_webhook import DiscordWebhook, DiscordEmbed # Send messages

token = "NzI4MjcwMzMwMjc5MjMxNTE4.Xv3-eQ.XtInoCnuq_sTkg9BH6viZD5b3Es"
client = discord.Client()

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
					return data; # Return json
					break # Send only one message
	return false
	
@client.event
async def on_message(message):
	if message.content.startswith('!meme'):
		data = memes() # Get json
		
		if data: # # Check if valid data
			temp = "by " + data['author'] + " on " + data['subreddit_name_prefixed'] + "\n" + str(data['ups']) + " likes - " + str(data['num_comments']) + " comments" # Footer
			embed = discord.Embed(color=random.randint(0, 16777215)) # Side color
			embed.set_author(name=data['title'], url='https://reddit.com' + data['permalink'], icon_url=data['thumbnail']) # Title
			embed.set_footer(text=temp) # Footer text
			embed.set_image(url=data['url']) # Image
			await message.channel.send(embed=embed) # Send message
			
		else:
			await message.channel.send("Error: Could not get meme")
			
client.run(token)

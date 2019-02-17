from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import os
import time

#API Credientials
customer_api_key = "ggvqRq0xDzO24BWoxF2szNNpC"
customer_api_key_sec = "XkMKDu90fbrwuVwPv1QctNKmIb2yMzCJesIgjtsWpPkR7KDxe9"
access_token = "1059616729213546497-UbrzedSjsvD0J2OdS6h0nTf2g4e4UF"
access_token_sec = "qurcdaSiGaWqKXNERV5t0j9iybFZzuJYf8rVMVfEXqvat"

#Authen the Keys
auth = OAuthHandler(consumer_key=customer_api_key, consumer_secret=customer_api_key_sec)
auth.set_access_token(key=access_token, secret=access_token_sec)
API_ACCESS = tweepy.API(auth)

#Directories
image_dir = "image_data"
news_data_container = "news_data"
url_file_name = "urls.txt"
image_file_urls = "image_urls.txt"
url_source_file = f"{news_data_container}/{url_file_name}"
image_url_source_file = f"{news_data_container}/{image_file_urls}"

#PlaceHolders
url_for_news = []
image_urls = []
#Function to append the URL's
def url_appendor(file):
	with open(file, "r") as r:
		for lines in r.read().split("\n"):
			url_for_news.append(lines)
url_appendor(file=url_source_file)

#Function to Append the Image URL's
def image_url_appender(txt_file):
	with open(txt_file, "r") as r:
		for lines in r.read().split("\n"):
			image_urls.append(lines)
image_url_appender(txt_file=image_url_source_file)

os.chdir(image_dir)
current_dir = os.getcwd()


#Tweepy API for Http Request to Twitter for Image Uploade.

for n, images in enumerate(os.listdir(current_dir)):
	
	#Uploading the Image With URL as Status
	API_ACCESS.update_with_media(images,status="For More: " + url_for_news[n]+"\nImages Linked: "+image_urls[n])
	time.sleep(3)
	
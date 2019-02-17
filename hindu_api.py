import requests
import os
import shutil
#Getting the News Data from the API(The Hindu)
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=ENTER YOUR API KEY')
response = requests.get(url)
json_container = response.json()
data_dir = "news_data"

#Removing the Data Contined Directory if it Exists
if not os.path.isfile(data_dir):
	shutil.rmtree(data_dir)

#Creating a Directory
os.mkdir(data_dir)

#Appending the Data to a File
with open(f"{data_dir}/news.txt","a") as f:
	for n in range(len(json_container['articles'])):
		f.write(json_container['articles'][n]['description']+" \n")

#Appending the Titles Data.
with open(f"{data_dir}/titles.txt","a") as f:
	for n in range(len(json_container['articles'])):
		f.write(json_container['articles'][n]['source']['name']+" \n")

#Appending the URL link to the News Atricles.
with open(f"{data_dir}/urls.txt","a") as f:
	for n in range(len(json_container['articles'])):
		f.write(json_container['articles'][n]['url']+" \n")

#Appending the Image Urls to txt file
with open(f"{data_dir}/image_urls.txt", "a") as f:
	for n in range(len(json_container['articles'])):
		f.write(json_container['articles'][n]['urlToImage']+" \n")

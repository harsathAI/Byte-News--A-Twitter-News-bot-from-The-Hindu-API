from PIL import Image,ImageFont, ImageDraw
import textwrap
import os 
import shutil

data_directory = "news_data"
img_directory = "image_data"

if os.path.exists(img_directory):
	shutil.rmtree(img_directory)

#Recreating the Directory.
os.mkdir(img_directory)

news_data = []
news_title = []

#Function to Append the Data from File to the Array Placeholders.
def append_data_onto_array(data_file, title_files):
	with open(data_file, "r")as r:
		for lines in r.read().split("\n"):
			news_data.append(lines)

	with open(title_files, "r")as r:
		for lines in r.read().split("\n"):
			news_title.append(lines)

append_data_onto_array(data_file=f"{data_directory}/news.txt", title_files=f"{data_directory}/titles.txt")
#Removing the Last Element from the Array.
del news_data[-1], news_title[-1]

def image_writer(text_data, text_title):
	global news_data, news_title
	font_type_title = ImageFont.truetype("OpenSans-LightItalic.ttf",45)
	#image = Image.open("carbon.png")
	font_type = ImageFont.truetype("OpenSans-Light.ttf",45)

	for news_datas,data_s in enumerate(news_data):
		for news_titles, data_t in enumerate(news_title):

			image = Image.open("carbon.png")
			draw = ImageDraw.Draw(image)

			text = textwrap.fill(data_s,width=55)

			w,h = font_type.getsize(text)
			draw.text(xy=(650,100), text=data_t, font=font_type_title)
			draw.text(xy=(200,200),text=text,fill=(0,171,169),font=font_type)
			image.save(f"{img_directory}/image_{news_datas}.png")

image_writer(text_data=news_data, text_title=news_title)


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import math
import textwrap

# PIL.ImageDraw.Draw.polygon(xy, fill=None, outline=None)

def delegate_area(text, pic):
	return null

def resize_img(image, new_width):
	bbox = image.getbbox()
	width  = bbox[2]
	length = bbox[3]
	aspect_ratio = float(width)/float(length)
	print bbox
	print "length: " + str(length)
	print "width:  " + str(width)
	print "aspect ratio: " + str(aspect_ratio) + ":1"

	new_height = int(new_width * aspect_ratio)

	print "new height: " + str(new_height)
	print "new width:  " + str(new_width)

	image = image.resize((new_height,new_width))
	return image

def read_txt_file(file_path):
	print "Reading text file..."
	with open(file_path, 'r') as txt_file:
		# data=txt_file.readlines() # use to get list
		data = txt_file.read().replace('\n', '')
		print "Text read: '" + data + "'"
	return data

def paste_pic(pic,img):
	pic = resize_img(pic, 700)
	box = (180,360)
	img.paste(pic, box=box, mask=None)

def place_text(img,text, draw):
	margin = 40
	offset = 40
	font = ImageFont.truetype("HelveticaNeue Light.ttf",60)

	chars_per_line = float(36)
	number_of_lines = int(math.ceil(len(text)/chars_per_line))
	print number_of_lines

	for line in textwrap.wrap(text, width=chars_per_line):
		draw.text((margin, offset), line, font=font, fill="black")
		offset += font.getsize(line)[1]

def main():
	file_path = raw_input("text file to use: ")
	file_path = "sample_text.txt" 	## TODO: remove line 
	image_path = raw_input("image to use: ")
	image_path = "sample_img.jpg"	## TODO: remove line
	length = width = 1080 

	background = Image.new("RGB", (length,width),(255,255,255))
	text = read_txt_file(file_path)
	pic = Image.open(image_path)
	draw = ImageDraw.Draw(background)
	place_text(background, text, draw)
	paste_pic(pic,background)
	background.save("meme.jpg")

main()

# length = width = 1080
# file_path = raw_input("text file to use: ")
# text = read_txt_file("sample_text.txt")
# font = ImageFont.truetype("HelveticaNeue Light.ttf",60)

# # im.resize((100,100))
# img=Image.new("RGB", (length,width),(255,255,255))
# draw = ImageDraw.Draw(img)
# margin = 40
# offset = 40
# for line in textwrap.wrap(text, width=36):
#     draw.text((margin, offset), line, font=font, fill="black")
#     offset += font.getsize(line)[1]

# image_path = raw_input("image to use: ")
# paste_pic("sample_img.jpg",img)
# draw = ImageDraw.Draw(img)

# img.save("meme.jpg")

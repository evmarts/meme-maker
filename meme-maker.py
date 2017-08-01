import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import math
import textwrap

# PIL.ImageDraw.Draw.polygon(xy, fill=None, outline=None)

def calculate_text_box_height(text):
	## adding one more line adds 72px to the text-box area
	## want 57px between text and pic
	chars_per_line = float(36)
	line_height = 72
	number_of_lines = int(math.ceil(len(text)/chars_per_line))
	text_box_height = 96 + number_of_lines*line_height
	print "text-box height: " + str(text_box_height)
	return text_box_height

def calculate_image_box(pic):
	pic_size = pic.getbbox()
	print "pic size: " + str(pic_size)

	return 0

def delegate_area(text, pic):
	text_box_height = calculate_text_box_height(text)
	image_box = calculate_image_box(pic)

	return 0

def resize_img(image, new_width):
	bbox = image.getbbox()
	width  = bbox[2]
	length = bbox[3]
	aspect_ratio = float(width)/float(length)
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
	box = (40,240)
	img.paste(pic, box=box, mask=None)

def place_text(img,text, draw):
	margin = 40
	offset = 40
	font = ImageFont.truetype("HelveticaNeue Light.ttf",60)

	chars_per_line = float(36)

	for line in textwrap.wrap(text, width=chars_per_line):
		draw.text((margin, offset), line, font=font, fill="black")
		offset += font.getsize(line)[1]

def main():
	file_path = raw_input("text file to use: ")
	file_path = "sample_text.txt" 	## TODO: remove line 
	image_path = raw_input("image to use: ")
	image_path = "sample_img.jpg"	## TODO: remove line
	length = width = 1080 

	text = read_txt_file(file_path)
	pic = Image.open(image_path)

	delegate_area(text, pic)

	background = Image.new("RGB", (length,width),(255,255,255))

	draw = ImageDraw.Draw(background)
	place_text(background, text, draw)
	paste_pic(pic,background)

	text_box = [(0,0),(1079,240)]
	draw.rectangle(text_box,fill=None, outline = 128)

	background.save("meme.jpg")

main()

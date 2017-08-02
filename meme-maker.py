import PIL
import math
import textwrap
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

## returns the contents of the .txt file at file_path as a string
def read_txt_file(file_path):
	with open(file_path, 'r') as txt_file:
		# data=txt_file.readlines() # use to get list
		data = txt_file.read().replace('\n', '')
	return data

## calculates the bounding area needed for the text-box
def calculate_text_bbox(text):
	chars_per_line = float(36)
	line_height = 72
	number_of_lines = int(math.ceil(len(text)/chars_per_line))
	text_box_height = number_of_lines*line_height
	return (1000, text_box_height)

## calculates the dimensions of the pic after resizing to match text-box width
## TODO: hardcoded 1000px
def get_new_pic_dim(pic):
	bbox = pic.getbbox()
	width  = bbox[2]
	height = bbox[3]
	aspect_ratio = float(width)/float(height)
	new_height = int(1000 / aspect_ratio)
	return (1000, new_height)

## calculates the bounding area needed for the content-box, i.e. the area taken
## up by the text-box and pic with appropriate spacing included
def calculate_content_bbox(text_bbox, pic_bbox, spacing):
	px_between_text_and_pic = spacing[0]
	margin = spacing[1]
	offset = spacing[2]
	content_bbox_width  = offset + pic_bbox[0] + offset
	content_bbox_height = margin + text_bbox[1] + px_between_text_and_pic + pic_bbox[1] + margin
	content_bbox = (content_bbox_width, content_bbox_height)
	return content_bbox

## places the given text string onto the given image with the correct spacing
def place_text(img, text, spacing):
	draw = ImageDraw.Draw(img)
	margin = spacing[1]
	offset = spacing[2]
	font = ImageFont.truetype("HelveticaNeue Light.ttf",60)
	chars_per_line = float(36)
	for line in textwrap.wrap(text, width=chars_per_line):
		draw.text((margin, offset), line, font=font, fill="black")
		offset += font.getsize(line)[1]

## resizes the given image according to the given width, maintaining aspect ratio
## TODO: redundant code here with get_new_pic_dim()
def resize_img(image, new_width):
	bbox = image.getbbox()
	width  = bbox[2]
	height = bbox[3]
	aspect_ratio = float(width)/float(height)
	new_height = int(new_width / aspect_ratio)
	image = image.resize((new_width,new_height))
	return image

## pastes the given pic onto the canvas with the appropriate spacing
def paste_pic(pic, canvas, spacing):
	px_between_text_and_pic = spacing[0]
	margin = spacing[1]
	text_bbox_width = spacing[3]
	text_bbox_height = spacing[4]
	pic = resize_img(pic, text_bbox_width)
	box = (margin, margin + text_bbox_height + px_between_text_and_pic)
	canvas.paste(pic, box=box, mask=None)

## TODO: extract functions
def main():
	file_path = raw_input("text file to use: ")
	file_path = "sample_text.txt"	 	## TODO: remove line 
	image_path = raw_input("image to use: ")
	image_path = "sample_pic_tall.jpg"	## TODO: remove line
	width = height = 1080
	margin = offset = 40
	px_between_text_and_pic = 57
	spacing = [px_between_text_and_pic, margin, offset]
	text = read_txt_file(file_path)
	pic = Image.open(image_path)
	text_bbox = calculate_text_bbox(text)
	text_bbox_width = text_bbox[0]
	text_bbox_height = text_bbox[1]
	spacing.append(text_bbox_width)
	spacing.append(text_bbox_height)
	pic_bbox = get_new_pic_dim(pic)
	content_bbox = calculate_content_bbox(text_bbox, pic_bbox, spacing)
	canvas = Image.new("RGB", (content_bbox[0], content_bbox[1]), (255,255,255))
	place_text(canvas, text, spacing)
	paste_pic(pic, canvas, spacing)
	max_demision = max(content_bbox)
	background = Image.new("RGB", (max_demision, max_demision), (255,255,255))
	box = [abs((content_bbox[0] - max_demision))/2, abs((content_bbox[1] - max_demision)/2)]
	background.paste(canvas, box=box, mask=None)
	background.resize((width,height))
	background.save("meme.jpg")
main()
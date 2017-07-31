import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap


def read_txt_file(file_path):
	print "Reading text file..."
	with open(file_path, 'r') as txt_file:
		# data=txt_file.readlines() # use to get list
		data = txt_file.read().replace('\n', '')
		print "Text read: '" + data + "'"
	return data

def paste_pic(im_path,img):
	pic = Image.open(im_path)
	pic = pic.resize((900,900))
	box = (180,360)
	img.paste(pic, box=box, mask=None)

def place_text(img,text, draw):
	margin = 40
	offset = 40
	font = ImageFont.truetype("HelveticaNeue Light.ttf",60)
	for line in textwrap.wrap(text, width=36):
		draw.text((margin, offset), line, font=font, fill="black")
		offset += font.getsize(line)[1]

def main():
	file_path = raw_input("text file to use: ")
	file_path = "sample_text.txt" 	## TODO: remove line 
	image_path = raw_input("image to use: ")
	image_path = "sample_img.jpg" ## TODO: remove line
	length = 1080 
	width = 1080

	img = Image.new("RGB", (length,width),(255,255,255))
	text = read_txt_file(file_path)
	draw = ImageDraw.Draw(img)
	place_text(img, text, draw)
	paste_pic(image_path,img)
	img.save("meme.jpg")

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


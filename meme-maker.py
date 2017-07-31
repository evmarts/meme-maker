import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap

def read_txt_file(file_path):
	print "Reading text file..."
	with open(file_path, 'r') as txt_file:
		data = txt_file.read().replace('\n', '')
		print "Text read: '" + data + "'"
	return data

def paste_pic(im_path,img):
	print "Pasting image..."
	pic = Image.open(im_path)
	pic = pic.resize((900,900))
	box = (180,360)
	img.paste(pic, box=box, mask=None)

def place_text(text, font, margin, offset, img):
	## TODO
	return 0

length = width = 1080
file_path = raw_input("text file to use: ")
text = read_txt_file("sample_text.txt")
font = ImageFont.truetype("HelveticaNeue Light.ttf",60)

# im = Image.open("img1.jpg")
# im.resize((100,100))
img=Image.new("RGB", (length,width),(255,255,255))
draw = ImageDraw.Draw(img)
margin = 40
offset = 40
for line in textwrap.wrap(text, width=36):
    draw.text((margin, offset), line, font=font, fill="black")
    offset += font.getsize(line)[1]

image_path = raw_input("image to use: ")
paste_pic("sample_img.jpg",img)
draw = ImageDraw.Draw(img)

img.save("meme.jpg")



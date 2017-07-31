import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap


def paste_pic(im_path,img):
	pic = Image.open(im_path)
	pic = pic.resize((900,900))
	box = (180,360)
	img.paste(pic, box=box, mask=None)

def place_text(text, font, margin, offset, img):
	## TODO
	return 0

length = width = 1080
text = "When you blah blah blah blah blah blah blah blah"
font = ImageFont.truetype("/Library/Fonts/HelveticaNeue Light.ttf",60)

# im = Image.open("img1.jpg")
# im.resize((100,100))
img=Image.new("RGBA", (length,width),(255,255,255))
draw = ImageDraw.Draw(img)
margin = 40
offset = 40
for line in textwrap.wrap(text, width=36):
    draw.text((margin, offset), line, font=font, fill="black")
    offset += font.getsize(line)[1]
paste_pic("img1.jpg",img)
draw = ImageDraw.Draw(img)

img.save("test.png")



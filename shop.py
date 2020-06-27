'''
Handles adding text to image
Sam Minix
6/26/20
'''
from PIL import Image, ImageDraw, ImageFont
#photo from https://ftw.usatoday.com/2017/05/what-is-spongebob-meme-mean-mocking-internet-chicken-episode-twitter-jokes
def shop(text):
    image = Image.open('mocking_spongebob.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('/opt/X11/share/fonts/TTF/VeraBd.ttf', size=45)
    color = 'rgb(255,255,255)'
    (x,y) = (50,50)

    draw.text((x,y), text, fill=color, font=font)
    image.show()
    
    

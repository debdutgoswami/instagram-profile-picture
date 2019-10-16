import urllib.error, urllib.parse, urllib.request
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import re, sys

def image_url(url, ctx):
    #header parameter is used to resolve the bad gateway 502 error
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    #opening the URL and parsing it into BeautifulSoup
    try:
        html = urllib.request.urlopen(req, context=ctx).read()
    except:
        print("Page not found or No internet connection")
        sys.exit()

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('body')

    #using regualr expression to extract the image URL
    profile_pic_url_hd = re.findall("profile_pic_url_hd\":\"([\S]+?)\"",str(tags[0]))[0]

    return profile_pic_url_hd

def image_show(profile_pic_url_hd, username):
    """opening the image from the the URL,
        saving the opened image

    Arguments:
        profile_pic_url_hd {string} -- profile pic url
    """

    response = urllib.request.urlopen(profile_pic_url_hd).read()
    img = Image.open(BytesIO(response))
    img.show()
    img.save("{}.png".format(username))
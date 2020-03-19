import requests
import urllib.parse
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import re, sys

def image(username):
    url = "https://www.instagram.com/{}/".format(username)

    session = requests.session()
    #header parameter is used to resolve the bad gateway 502 error
    #html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

    #opening the URL and parsing it into BeautifulSoup
    try:
        html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    except:
        print("Page not found or No internet connection")
        sys.exit()

    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('body')

    #using regualr expression to extract the image URL
    profile_pic_url_hd = re.findall(r"profile_pic_url_hd\":\"([\S]+?)\"",str(tags[0]))[0].replace(r'\u0026', '&')

    response = session.get(profile_pic_url_hd, headers={'User-Agent': 'Mozilla/5.0'}).content
    img = Image.open(BytesIO(response))
    img.show()
    img.save("{}.png".format(username))


#custom imports
import username,  re
import ProfileImage as pi

url = username.user_url()
usname = re.findall(r"https:\/\/www.instagram.com\/([\S]+?)\/", url)[0]

pi.image(url, usname)
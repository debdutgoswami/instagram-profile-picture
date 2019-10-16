#custom imports
import username, certificate
import ProfileImage as pi

url = username.user_url()
ctx = certificate.context_ssl() #this step is not mandatory but advicable

profile_pic_url_hd = pi.image_url(url, ctx)
pi.image_show(profile_pic_url_hd) #opens the image in a new window and also saves the image in the working directory
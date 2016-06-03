import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://images.nationalgeographic.com/wpf/media-live/photos/000/936/cache/bear-road-denali_93621_990x742.jpg")
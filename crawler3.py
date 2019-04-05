import requests 
from pytube import YouTube
image_url = "http://darwoft.com/wp-content/themes/darwoftTheme/img/logo_darwoft.png"
  
r = requests.get(image_url) 
with open("docs/darwoft/darwoft.png",'wb') as f: 
  
    f.write(r.content) 

YouTube('https://www.youtube.com/watch?v=ftVLTF1NjYw').streams.first().download('docs/darwoft/')



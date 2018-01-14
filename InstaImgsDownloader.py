from bs4 import BeautifulSoup
from datetime import datetime
import requests
import urllib
import re

def downloadImages(URL):
     r=requests.get(URL)
     soup=BeautifulSoup(r.content,'html5lib')
     jsContent=soup.findAll('script',attrs={'type':'text/javascript'})[2].string
     imageLinks=re.findall(r'(https?://\S+640x640\S+.jpg)', str(jsContent))
     for image in imageLinks:
          urllib.request.urlretrieve(image,datetime.now().strftime('%Y%m%d%H%M%S')+".jpg")

downloadImages("https://www.instagram.com/art.by.sripooja")

'''
Please NOTE:
--------------------
This code is just the first version. Lot of improvements are yet to be done.
Following changes have to be done:
1. All images are not getting downloaded from a public instagram account using this code and few images are getting downloaded twice. Code has to be modified in order to download all the images.
2. The downloaded files are saved in the directory where the code exists. Download method must have an argument for providing folder path where the files have to be downloaded.
3. The files must be ZIPPED so that it is easy for the user to extract when required rather than downloading all the images directly.
4. Some public accounts have a large number of images so a limit for downloading images has to be provided.

Common issues one might face (based on my experience):
----------------------------------------------------------------------------------
1. importing uninstalled packages (like bs4, requests, html5lib etc)
2. install "pip" the package management tool for Python
3. if all the library files are installed but you are still getting any version/import errors then try ugrading the packages installed. The command for upgrading the packages is "pip install --upgrade <pkgname>"

Useful links to follow - https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
'''

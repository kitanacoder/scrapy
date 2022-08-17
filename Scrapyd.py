#import html5lib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

def skrapper():
	print('---- start Skrapper ----')
	#html = urlopen("https://comfy.ua")
	html = urlopen("https://dveri.zp.ua")
	#html = urlopen("https://eldorado.ua")
	#html = urlopen("https://")
	bsObj = BeautifulSoup(html.read(), 'html.parser')
	#bsObj = BeautifulSoup('features="html5lib"')
	#nameList = bsObj.findAll("span", {"class":"green", "class":"red"})
	nameList = bsObj.findAll()
	for name in nameList:
		print(name.get_text())
	print('---- end Skrapper ----')


if __name__ == "__main__":
	skrapper()
	print('---- hellow Im Works ----')
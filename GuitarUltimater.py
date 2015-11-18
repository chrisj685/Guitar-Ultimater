from gettabs import *
from urllib import *
from lxml.etree import tostring

""" 
	This program will take a song title as an input and output
	the text of the most common tab from ultimate guitar
	It uses pygoogle to search for the tabs
	
	Language: Python 3
	Author: Chris Johnson
"""

def readUG(url):
	"""
	site = request.urlopen(url).read()
	
	start = 0
	end = 0
	for i in range(0, len(site)):
		if site[i:i+12] == "<pre><i></i>":
			print('BBBBBBBBBBBBBBBBBBBBBBBBBb')
			start = i+12
		if site[i:i+6] == '</pre>' and start != 0 and i > start:
			print("AAAAAAAAAAAAAAAAAAAAAAAA")
			end = i
			break
		print(start)
	return site[start:end] """

	page = requests.get(url)
	tree = html.fromstring(page.content)
	tab = tree.xpath('//div[@id="cont"]//pre')
	return tostring(tab[2])
	
def search(song, ttype):
	otabs = getTabs(song)
	tabs = []
	
	for tab in otabs:
		if (tab.ttype == ttype):
			tabs.append(tab)
	return tabs


if __name__ == '__main__':
	song = input("Enter song title: ")
	tabs = search(song, "tab")
	for tab in tabs:
		print(tab.link + ", " + tab.ttype)
	print(readUG(tabs[0].link))

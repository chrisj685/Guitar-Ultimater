from lxml import html
import requests
"""
	A class that contains data for a guitar tab
	Contains the link, song title, and artist
"""
class Tab:
	link = ''
	title = ''
	artist = ''
	ttype = ''

	def __init__(self, link, title, ttype):
		self.link = link
		self.title = title
		self.ttype = ttype

def getTabs(title):
	# list of every tab found
	ot = title
	tabs = []

	# format title
	i = 0
	while (i < len(title)):
		if title[i] == ' ':
			title = title[:i] + '+' + title[i+1:]
		i += 1

	# request the search page from ultimate guitar
	page = requests.get('https://www.ultimate-guitar.com/search.php?search_type=title&value=' + title)
	tree = html.fromstring(page.content)
	links = tree.xpath('//body//a/@href')

	# filter out the useless links
	tabs = []
	for i in links:
		i = str(i)
		
		if (i.endswith('tab.htm') or i.endswith('crd.htm')) and not i.endswith('power_tab.htm'):
			# get information from tab page

			if i.endswith('btab.htm'): ttype = 'bass'
			elif i.endswith('crd.htm'): ttype = 'chords'
			elif i.endswith('ukulele_crd.htm'): ttype = 'uke chords'
			else: ttype = 'tab'

			# create and add tab object to tabs 
			#tabs.append(Tab(i, title, ttype))
			tabs.append(Tab(i, ot, ttype))
	return tabs



"""
	Test for getTabs and Tab
"""
if __name__ == "__main__":
	t = getTabs("Purple Haze")
	#print(t[0].title[0].items())
	for tab in t:
		print(tab.title)
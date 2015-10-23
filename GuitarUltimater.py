from urllib import *
import urllib
import json
from pygoogle import pygoogle

""" 
	This program will take a song title as an input and output
	the text of the most common tab from ultimate guitar
	It uses pygoogle to search for the tabs
	
	Language: Python 2
	Author: Chris Johnson
"""

url = 'http://tabs.ultimate-guitar.com/j/jimi_hendrix/purple_haze_tab.htm'

def readUG(url):
	site = urlopen(url).read()
	start = 0
	end = 0
	for i in range(0, len(site)):
		if site[i:i+12] == '<pre><i></i>':
			start = i+12
		if site[i:i+6] == '</pre>' and start != 0:
			end = i
			break
	return site[start:end]
	print start, end
	
def search(song):
	query = urllib.urlencode({'q': search})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	search_response = urllib.urlopen(url)
	search_results = search_response.read()
	results = json.loads(search_results)
	data = results['responseData']
	#print 'Total results: %s' % data['cursor']['estimatedResultCount']
	hits = data['results']
	print 'Top %d hits:' % len(hits)
	for h in hits: print ' ', h['url']
	#print 'For more results, see %s' % data['cursor']['moreResultsUrl']

	"""
	search = pygoogle(song + ' guitar tab')
	urls = search.get_urls()
	for url in urls:
		if 'ultimate-guitar' in url:
			return url
	"""
	
if __name__ == '__main__':
	song = raw_input("Enter song title: ")
	search(song)
	#print readUG(search(url))

# get news pages that I am interested in 
# in this case, all news about AMD
from xml.dom.minidom import parse
import re
import xml.dom.minidom
import os

# read all xml files in current directory
patternF  = '.*\.xml'
allFiles = next(os.walk('.'))[2]

for file in allFiles:
	matchF = re.search(patternF, file)
	if matchF:
		xmlFile = matchF.group()
		# Open XML document using minidom parser
		DOMTree = xml.dom.minidom.parse(xmlFile)
		collection = DOMTree.documentElement
		
		# titles could be AMD or AMD's
		patternUrlList = ['.*\-amd\-.*','.*\-amds\-.*']
		urls = collection.getElementsByTagName("url")

		# Print url of interested news for content crawler
		for address in urls:
			url = address.getElementsByTagName('loc')[0]
			url = url.childNodes[0].data

			for p in patternUrlList:
				matchU = re.search(p,url)
				if matchU:
					new_url = matchU.group()
					print ("%s" % new_url)
			
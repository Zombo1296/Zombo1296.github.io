# to get sitemap.xmls
from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
# Most of the time, the sitemap xml is index
# wget bash script handles exceptions
DOMTree = xml.dom.minidom.parse("index.xml")
collection = DOMTree.documentElement

maps = collection.getElementsByTagName("sitemap")

fileList = []

# Print xml file address of each site.
for site in maps:
	xmlFile = site.getElementsByTagName('loc')[0]
	xmlFile = xmlFile.childNodes[0].data
	fileList.append(xmlFile)

fileList.sort()

# will redirect by >
for x in fileList:
	print(x)
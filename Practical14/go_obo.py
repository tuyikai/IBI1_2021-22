from xml.dom.minidom import parse 
import xml.dom.minidom
n=0
m=0
DOMTree = xml.dom.minidom.parse('F:\Python\Practical14\go_obo.xml')
collection = DOMTree.documentElement
ids = collection.getElementsByTagName('id')
if collection.hasAttribute("id"): 
        print ("id")
        collection.getAttribute("name")
for id in ids:
    n +=1

terms = collection.getElementsByTagName('term')
for term in terms:
    m +=1
print('the number of term is ',m)
print('the number of id is',n)
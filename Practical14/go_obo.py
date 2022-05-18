from xml.dom.minidom import parse 
import xml.dom.minidom
n=0
m=0
DOMTree = xml.dom.minidom.parse('F:\Python\Practical14\go_obo.xml')
collection = DOMTree.documentElement
ids = collection.getElementsByTagName('id')#this form enable us to use xml data
if collection.hasAttribute("id"): 
        print ("id")
        collection.getAttribute("name")
for id in ids:
    n +=1

terms = collection.getElementsByTagName('term')#print(type(names))
for term in terms:
    m +=1
for i in range(len(ids)): 
    print(ids[i].firstChild.data)             #循坏读取列表中的内容跟    #打印节点数据
    print(ids[i].getAttribute('is_a'))#show the result
print('the number of term is ',m)
print('the number of id is',n)
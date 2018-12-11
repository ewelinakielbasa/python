from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("2_3.xml")
collection = DOMTree.documentElement

CDs = collection.getElementsByTagName("CD")
for cd in CDs:
    print("--CD--")
    if cd.hasAttribute("id"):
        print("ID: " + cd.getAttribute("id"))
        title = cd.getElementsByTagName('TITLE')[0]
        print("title: " + title.childNodes[0].data)
        artist = cd.getElementsByTagName('ARTIST')[0]
        print("artist: " + artist.childNodes[0].data)
        country = cd.getElementsByTagName('COUNTRY')[0]
        print("country: " + country.childNodes[0].data)
        company = cd.getElementsByTagName('COMPANY')[0]
        print("company: " + company.childNodes[0].data)
        price = cd.getElementsByTagName('PRICE')[0]
        print("price: " + price.childNodes[0].data)
        year = cd.getElementsByTagName('YEAR')[0]
        print("year: " + year.childNodes[0].data)


def replace(collection, node, nodeValue, newText):
    CDs = collection.getElementsByTagName("CD")
    for cd in CDs:
        if cd.hasAttribute("id"):

            if cd.getElementsByTagName(node)[0].childNodes[0].data == nodeValue:

                cd.getElementsByTagName(node)[0].childNodes[0].replaceWholeText(newText)


replace(collection, 'YEAR', '1982', '--NEW DATA--')
file_handle = open("2_3new.xml", "w")
collection.writexml(file_handle)
file_handle.close()





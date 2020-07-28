import os
import re

class Scraper:

    urlDict = {'mask'    : 'https://www.ebay.com/sch/?_nkw=face-mask&_pgn=',
               'handSan' : 'https://www.ebay.com/sch/?_nkw=Hand-Sanitizer&_pgn=',
               'ebay'    : 'https://www.ebay.com/sch/i.html?_nkw='}
    

    def __init__(self, item):
        self.item = item

    def scrapePage(self, numPage):
        stream = os.popen('wget -qO- '+self.urlDict[self.item]+str(numPage))
        out = stream.read()
        itemArr = re.findall(r'<li class="s-item(.*?)<\/li>', out)
        
        tempItmDict = []

        i=0

        for x in itemArr:
            name = str(re.findall(r'alt="(.*?)"', x))
            price = str(re.findall(r'<span class=s-item__price>(.*?)<\/span>', x))
            url = str(re.findall(r'href=(.*?)\?', x)[0])
            rating = re.findall(r'<span class=clipped>(.*?) out of', x)
            numSold = re.findall(r'<span class="BOLD NEGATIVE">(.*?)<\/span>', x)
            img = re.findall(r'src=(.*?)\s', x)

            nameLength = len(name)
            imgLength = len(img)
            plength = len(price)

            if name[0:7] == "['<span":
                name = name[21:nameLength-9]
            else:
                name = name[2:nameLength-2]

            if imgLength > 1:
                img = img[1]
            else:
                img = img[0]

            if plength < 28:
                price = float(price[3:plength-2])
            else:
                price = float(price[3:plength-28])

            if rating == []:
                rating = 'None'

            if numSold == []:
                numSold = 'None'

            tempItmDict += [{
                'itemType' : self.item,
                'name'     : name,
                'price'    : price,
                'url'      : url,
                'rating'   : rating,
                'numSold'  : numSold,
                'img'      : img
            }]
            
            i += 1

        return tempItmDict
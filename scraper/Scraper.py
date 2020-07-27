import os
import re

class Scraper:

    urlDict = {'mask' : 'https://www.ebay.com/b/face-mask/bn_7024874153?_pgn='}
    

    def __init__(self, item):
        self.item = item

    def scrapePage(self, numPage):
        cmd = 'wget -O crawl.html '+self.urlDict['mask']+str(numPage)
        os.system(cmd)
        f = open("crawl.html", 'r')
        itemArr = []
        for i in f:
            tempArr = re.findall(r'<li class=\"s-item(.*?)<\/li>', i)
            if tempArr != []:
                itemArr += tempArr
        
        tempItmDict = []

        i=0

        for x in itemArr:
            name = str(re.findall(r'<h3 class="s-item__title">(.*?)<\/h3>', x))
            price = str(re.findall(r'<span class="s-item__price">(.*?)<\/span>', x))
            url = str(re.findall(r'href="(.*?)\?', x)[0])
            rating = re.findall(r'<span class="clipped">(.*?) out of', x)
            numSold = re.findall(r'<span class="NEGATIVE">(.*?)<\/span>', x)

            plength = len(price)

            if plength < 28:
                price = float(price[3:plength-2])
            else:
                price = float(price[3:plength-28])

            if rating == []:
                rating = 'None'

            if numSold == []:
                numSold = 'None'

#            print('Name: '+ str(name)+'Price: '+str(price))
#            print(numSold)

            tempItmDict += [{
                'name'    : name,
                'price'   : price,
                'url'     : url,
                'rating'  : rating,
                'numSold' : numSold
            }]
            
            i += 1

        return tempItmDict
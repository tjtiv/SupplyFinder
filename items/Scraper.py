import os
import re
import requests
import concurrent.futures

from .models import Item


class Scraper:

    urlDict = {'ebay'    : 'https://www.ebay.com/sch/i.html?_nkw='}
    

    def __init__(self, item):
        self.item = item

    def scrapePage(self, numPage):
        
        tempItmDict = []

        url = self.urlDict['ebay']+self.item+'&_pgn='+str(numPage)

        pageBytes = requests.get(url).content
        pageText = pageBytes.decode('utf-8')
        itemArr = re.findall(r'<li class="s-item(.*?)<\/li>', pageText)

        i=0

        for x in itemArr:
            name = str(re.findall(r'alt="(.*?)"', x))
            price = str(re.findall(r'<span class=s-item__price>(.*?)<\/span>', x))
            url = str(re.findall(r'href=(.*?)\?', x)[0])
            rating = re.findall(r'<span class=clipped>(.*?) out of', x)
            numSold = re.findall(r'<span class="BOLD NEGATIVE">(\d*.\d*).*?<\/span>', x)
            img = re.findall(r'src=(.*?)\s', x)
            shipping = re.findall(r'<span class="s-item__shipping s-item__logisticsCost">(.*?)<\/span>', x)

            nameLength = len(name)
            imgLength = len(img)
            plength = len(price)
            shipLength = len(shipping)

            if name[0:7] == "['<span":
                name = name[21:nameLength-9]
            else:
                name = name[2:nameLength-2]

            if imgLength > 1:
                img = img[1]
            else:
                img = img[0]

            if plength < 28:
                price = round(float(price[3:plength-2]), 2)
            else:
                price = round(float(price[3:plength-28]), 2)

            if rating == []:
                rating = 0
            else:
                rating = float(rating[0])

            if numSold == [] or (numSold[0])[0].isalpha():
                numSold = 0
            elif (numSold[0])[-1] == '+':
                numSold = int((numSold[0])[0:-1])
            elif len(numSold[0]) < 4:
                numSold = int(numSold[0])
            else:
                numSold = int(numSold[0].replace(',',''))

            if shipping == [] or shipping[0] == 'Free shipping':
                shipping = 0
            else:
                shipping = float((shipping[0])[3:shipLength-9])

            tempItmDict += [{
                'itemType' : self.item,
                'name'     : name,
                'price'    : price,
                'url'      : url,
                'rating'   : rating,
                'numSold'  : numSold,
                'img'      : img,
                'shipping' : shipping
            }]
            
            i += 1

        return tempItmDict


    def scrapePageRange(self, pgRange):
        for i in pgRange:
            scrapeDict = self.scrapePage(i)
            #print(len(scrapeDict))
            for j in scrapeDict:
                Item.objects.create( itemType = self.item, 
                                    name     = j['name'], 
                                    price    = j['price'], 
                                    url      = j['url'], 
                                    rating   = j['rating'],  
                                    numSold  = j['numSold'], 
                                    img      = j['img'], 
                                    shipping = j['shipping'],
                                    score = 0 )


    def createScrapeThreads(self):
        pageRangeList = [
            range(1, 11),
            range(11, 21),
            range(21, 31),
            range(31, 41),
            range(41, 51),
            range(51, 61),
            range(61, 71),
            range(71, 81),
            range(91, 101)
        ]

        with concurrent.futures.ThreadPoolExecutor() as ex:
            ex.map(self.scrapePageRange, pageRangeList)
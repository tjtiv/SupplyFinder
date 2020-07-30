from django.shortcuts import render
from scraper.Scraper import Scraper
#from scraper.Analyzer import Analyzer
from .models import Item
from django.db.models import Avg

def item_view(response, *args, **kwargs):
   itm = response.GET['itm']
   scarper = Scraper(itm)

#   for i in range(1, 2):
#      scrapeDict = scarper.scrapePage(i)
#
#      for j in scrapeDict:
#         Item.objects.create( itemType = itm, 
#                              name     = j['name'], 
#                              price    = j['price'], 
#                              url      = j['url'], 
#                              rating   = j['rating'],  
#                              numSold  = j['numSold'], 
#                              img      = j['img'], 
#                              shipping = j['shipping'] )
   
   avgPrice = Item.objects.all().filter(itemType=itm).aggregate(Avg('price'))
   
#   itmLst = Item.objects.all()

   itmLst = Item.objects.order_by('price').filter(itemType=itm)

   con = {
      'avg'     : avgPrice['price__avg'],
      'itmLst'  : itmLst
   }

   return render(response, "items.html", con)

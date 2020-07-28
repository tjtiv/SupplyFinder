from django.shortcuts import render
from scraper.Scraper import Scraper
from .models import Item
from django.db.models import Avg

def item_view(response, *args, **kwargs):
   itm = response.GET['itm']
   scarper = Scraper(itm)

   print("RESPPPPP!!!: "+str(response.GET))

   for i in range(0, 2):
      scrapeDict = scarper.scrapePage(i)

      for j in scrapeDict:
         Item.objects.create(itemType=itm, name=j['name'], price=j['price'], url=j['url'], rating=j['rating'],  numSold=j['numSold'], img=j['img'])
   
   avgPrice = Item.objects.all().filter(itemType=itm).aggregate(Avg('price'))
   
#   itmLst = Item.objects.all()

   itmLst = Item.objects.order_by('price').filter(itemType=itm)

   con = {
      'avg'     : avgPrice['price__avg'],
      'itmLst'  : itmLst
   }

   return render(response, "items.html", con)

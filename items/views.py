from django.shortcuts import render
from scraper.Scraper import Scraper
from .models import Item
from django.db.models import Avg

def mask_view(response, *args, **kwargs):
   scarper = Scraper("mask")


#   for i in range(0, 21):
#      scrapeDict = scarper.scrapePage(i)
#
#      for j in scrapeDict:
#         Item.objects.create(name=j['name'], price=j['price'], url=j['url'], rating=j['rating'],  numSold=j['numSold'])
   
   avgPrice = Item.objects.all().aggregate(Avg('price'))
   
   itmLst = Item.objects.all()

   con = {
      'avg'     : avgPrice['price__avg'],
      'itmLst'  : itmLst
   }

   return render(response, "mask.html", con)

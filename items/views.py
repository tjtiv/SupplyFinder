from django.shortcuts import render
from .Scraper import Scraper
from .models import Item
from django.db.models import Avg

def item_view(response, *args, **kwargs):
   itm = response.GET['itm']

   scarper = Scraper(itm)
   scarper.createScrapeThreads()

   avgPrice = Item.objects.all().filter(itemType=itm).aggregate(Avg('price'))
   itmLst = Item.objects.order_by('name').filter(itemType=itm)

   con = {
      'avg'     : avgPrice['price__avg'],
      'itmLst'  : itmLst
   }

   return render(response, "items.html", con)

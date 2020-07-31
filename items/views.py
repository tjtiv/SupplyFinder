from django.shortcuts import render
from .models import Item
from django.db.models import Avg
from .Scraper import Scraper
from .Analyzer import Analyzer

def item_view(response, *args, **kwargs):
   itm = response.GET['itm']
   sort = response.GET['sort']

#   scarper = Scraper(itm)
#   scarper.createScrapeThreads()
#   scarper.scrapePageRange(range(1,3))

#   analyzer = Analyzer(Item.objects.all().filter(itemType=itm))
#   analyzer.findItemScore()

   avgPrice = Item.objects.all().filter(itemType=itm).aggregate(Avg('price'))
   
   if sort == 'score':
      itmLst = Item.objects.order_by('-score').filter(itemType=itm)
   elif sort == 'name':
      itmLst = Item.objects.order_by('name').filter(itemType=itm)
   elif sort == 'price':
      itmLst = Item.objects.order_by('price').filter(itemType=itm)
   elif sort == 'rating':
      itmLst = Item.objects.order_by('-rating').filter(itemType=itm)
   elif sort == 'sold':
      itmLst = Item.objects.order_by('-numSold').filter(itemType=itm)
   
   con = {
      'avg'     : round(avgPrice['price__avg'], 2),
      'itmLst'  : itmLst,
      'itm'     : itm
   }

   return render(response, "items.html", con)

from django.shortcuts import render
from .models import Item
from django.db.models import Avg
from .Scraper import Scraper
from .Analyzer import Analyzer

def item_view(response, *args, **kwargs):
   itm = response.GET['itm']
   sort = response.GET['sort']
   pg = int(response.GET['pg'])
   scrapeFlag = response.GET['scrp']

   startIndex = pg*30
   endIndex = startIndex+31

   if scrapeFlag == 'True':
      scarper = Scraper(itm)
      scarper.createScrapeThreads()

      analyzer = Analyzer(Item.objects.all().filter(itemType=itm))
      analyzer.findItemScore()

   avgPrice = Item.objects.all().filter(itemType=itm).aggregate(Avg('price'))
   
   if sort == 'score':
      itmLst = Item.objects.order_by('-score').filter(itemType=itm)[startIndex : endIndex]
   elif sort == 'name':
      itmLst = Item.objects.order_by('name').filter(itemType=itm)[startIndex : endIndex]
   elif sort == 'price':
      itmLst = Item.objects.order_by('price').filter(itemType=itm)[startIndex : endIndex]
   elif sort == 'rating':
      itmLst = Item.objects.order_by('-rating').filter(itemType=itm)[startIndex : endIndex]
   elif sort == 'sold':
      itmLst = Item.objects.order_by('-numSold').filter(itemType=itm)[startIndex : endIndex]
   
   con = {
      'avg'     : round(avgPrice['price__avg'], 2),
      'itmLst'  : itmLst,
      'itm'     : itm,
      'pg'      : pg,
      'scrp'    : scrapeFlag,
      'sort'    : sort
   }

   return render(response, "items.html", con)

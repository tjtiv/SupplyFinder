from .models import Item
from django.db.models import Sum

class Analyzer:

    def __init__(self, itmLst):
        self.itmLst = itmLst


    def findItemScore(self):
        for item in self.itmLst:
            
            
            try:
                totalSold = float(self.itmLst.aggregate(Sum('numSold'))['numSold__sum'])
                soldScore = float(item.numSold/totalSold)
                itemPrice = float(item.price + item.shipping)
                ratingScore = float(item.rating/5)
                itemScore = (ratingScore + soldScore) / itemPrice
            except Exception as e:
                itemScore = 0
            
            #if item.rating == 0:
            #    ratingScore = 0
            #else:
            #    ratingScore = float(item.rating/5)

            #if (ratingScore+soldScore) == 0:
            #    itemScore = 0
            #else:
            #    itemScore = (ratingScore + soldScore) / itemPrice

            item.score = itemScore
            item.save()

        #for i in sortedPrice:
        #    i.pricePos=



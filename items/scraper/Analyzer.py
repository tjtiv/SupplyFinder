import numpy as np

class Analyzer:

    def __init__(self, itmLst):
        self.itmLst = itmLst


    def createItmGraph(self, num, sortedSold, sortedPrice):
        itemMatrix = np.zeros((num,num))

        #for i in sortedPrice:
        #    i.pricePos=



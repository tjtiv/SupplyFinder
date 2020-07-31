from django.db import models

class Item(models.Model):
    itemType = models.TextField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    url = models.TextField()
    rating = models.FloatField()
    numSold = models.IntegerField()
    img = models.TextField()
    shipping = models.FloatField()
    score = models.FloatField()

    def __str__(self):
        return self.name

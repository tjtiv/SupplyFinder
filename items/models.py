from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    url = models.TextField()
    rating = models.TextField()
    numSold = models.TextField()


    def __str__(self):
        return self.name

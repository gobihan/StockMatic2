from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=2048)
    symbol = models.CharField(max_length=2048, unique=True)
    sector = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

class StockData(models.Model):
    stock = models.ForeignKey(
        to=Stock,
        related_name='data',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    open_price = models.DecimalField(max_digits=5, decimal_places=2)
    close_price = models.DecimalField(max_digits=5, decimal_places=2)
    high_price = models.DecimalField(max_digits=5, decimal_places=2)
    low_price = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.IntegerField(default=0)

    def __str__(self):
        return self.stock.name +" "+ str(self.date)
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Part(models.Model):
    item = models.ForeignKey('items.Item', related_name='parts')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

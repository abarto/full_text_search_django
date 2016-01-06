from django.db import models


class ItemQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "MATCH (name) AGAINST (%s IN NATURAL LANGUAGE MODE)"},
            select_params=(name,),
            where=('MATCH (name) AGAINST (%s IN NATURAL LANGUAGE MODE) > 0',),
            params=(name,),
            order_by=('-rank',)
        )

    def text_search_part_name(self, name):
        return self.filter(id__in=Part.objects.text_search_name(name))


class PartQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "MATCH (name) AGAINST (%s IN NATURAL LANGUAGE MODE)"},
            select_params=(name,),
            where=('MATCH (name) AGAINST (%s IN NATURAL LANGUAGE MODE) > 0',),
            params=(name,),
            order_by=('-rank',)
        )

    def text_search_item_name(self, name):
        return self.select_related().extra(
            select={'rank': "MATCH (items_item.name) AGAINST (%s IN NATURAL LANGUAGE MODE)"},
            select_params=(name,),
            where=('MATCH (items_item.name) AGAINST (%s IN NATURAL LANGUAGE MODE) > 0',),
            params=(name,),
            order_by=('-rank',)
        )


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)

    objects = ItemQueryset.as_manager()

    def __str__(self):
        return self.name


class Part(models.Model):
    item = models.ForeignKey('items.Item', related_name='parts')
    name = models.CharField(max_length=200)

    objects = PartQueryset.as_manager()

    def __str__(self):
        return self.name

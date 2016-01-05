from django.db import models


class ItemQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "ts_rank_cd(to_tsvector('english', name), to_tsquery(%s), 32)"},
            select_params=(name,),
            where=("to_tsvector('english', name) @@ to_tsquery(%s)",),
            params=(name,),
            order_by=('-rank',)
        )


class PartQueryset(models.QuerySet):
    def text_search_name(self, name):
        return self.extra(
            select={'rank': "ts_rank_cd(to_tsvector('english', name), to_tsquery(%s), 32)"},
            select_params=(name,),
            where=("to_tsvector('english', name) @@ to_tsquery(%s)",),
            params=(name,),
            order_by=('-rank',)
        )

    def text_search_item_name(self, name):
        return self.select_related().extra(
            select={'rank': "ts_rank_cd(to_tsvector('english', items_item.name), to_tsquery(%s), 32)"},
            select_params=(name,),
            where=("to_tsvector('english', items_item.name) @@ to_tsquery(%s)",),
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

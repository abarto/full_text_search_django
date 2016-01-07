full_text_search_django
=======================

Introduction
------------

This project was created to provide an example on how to implement full text search in a `Django <https://www.djangoproject.com/>`_ site without using an external indexing solution like `Haystack <http://haystacksearch.org/>`.

Although having a specialized indexing solution is what most experts recommend when dealing with large, real word sites, sometimes it can be overkill if we're only working on a simple system with few users and models or if you lack the resources or expertise to manage an additional external dependency.

Most modern relational databases have some sort of full text search functionality. We'll show you how to take advantage of this to provide full text search on a `Django <https://www.djangoproject.com/>`_ site using the database back-ends. We chose `PostgreSQL <http://www.postgresql.org/>`_ and `MySQL <https://www.mysql.com/>`_ (and by extension `MariaDB <https://mariadb.org/>`_) given their popularity and ease of implementation of full text search indexes. The solution is quite simple, and can be adapted for other database back-ends.

The application
---------------

The application is just a plain old Django site with a single application named "items", which has the following model:

::

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

Just two models that refer to each other (so I can show you how to use full text search with related models).

Full Text Search with PostgreSQL
--------------------------------

Starting with version `8.3 <http://www.postgresql.org/docs/8.3/static/release-8-3.html>`_ introduced fully featured full text search capabilities. The system is `quite flexible <http://www.postgresql.org/docs/9.4/static/textsearch-intro.html>`_ and easy to use if you just want the default configuration for the English language (which I'll use here).

As shown in the `documentation <http://www.postgresql.org/docs/9.4/static/textsearch-tables.html#TEXTSEARCH-TABLES-SEARCH>`_, searching a table is quite simple:

::

    SELECT title
    FROM pgweb
    WHERE to_tsvector('english', body) @@ to_tsquery('english', 'friend');

In this example, the user is looking for 'friend' on the 'body' column of the 'pgweb' table using the 'english' configuration. We can easily adapt this to query a Django model, but first we can speed things up by creating an index on the columns that we want to query. We'll create our index using a migration:

::

    class Migration(migrations.Migration):

        dependencies = [
            ('items', '0001_initial'),
        ]

        operations = [
            migrations.RunSQL(
                "CREATE INDEX items_item_name_ts_idx ON items_item USING gin(to_tsvector('english', name));"
                "DROP INDEX IF EXISTS items_item_name_ts_idx;"
            ),
            migrations.RunSQL(
                "CREATE INDEX items_part_name_ts_idx ON items_part USING gin(to_tsvector('english', name));"
                "DROP INDEX IF EXISTS items_part_name_ts_idx;"
            ),
        ]

We're creating two indexes here: one for the ``Item``'s name and one for the ``Part``'s name. As mentioned in the PostgreSQL `documentation <http://www.postgresql.org/docs/9.4/static/textsearch-tables.html#TEXTSEARCH-TABLES-INDEX>`_, as long as the queries use the same ``ts_vector`` configuration, the index will be used. Next, we'll write the Django ORM queries for the ``Item`` and ``Part`` models as ``QuerySet``:

::

    class ItemQueryset(models.QuerySet):
        def text_search_name(self, name):
            return self.extra(
                select={'rank': "ts_rank_cd(to_tsvector('english', name), to_tsquery(%s), 32)"},
                select_params=(name,),
                where=("to_tsvector('english', name) @@ to_tsquery(%s)",),
                params=(name,),
                order_by=('-rank',)
            )

        def text_search_part_name(self, name):
            return self.filter(parts__id__in=Part.objects.text_search_name(name))


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

We made use of the ``QuerySet`` `extra <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#extra>`_ modifier to express the full text search queries. The ``text_search_name`` methods use a similar query to the one in the example, with a simple modification: We use PostgreSQL's `ts_rank_cd <http://www.postgresql.org/docs/9.4/static/functions-textsearch.html>`_ function to define a ranking between the matches, which allows us to order the results, which is what we want in these cases. Notice that I use the 'english' configuration so the indexes created in the migration are properly used. Be aware that if you use a different configuration **the query won't fail**, but it will not use the index.

The ``text_search_item_name`` and ``text_search_part_name`` shows you how to use the full text search with related tables. In ``text_search_item_name``, we're looking for Part objects whose related Item matches a specific text search query on its name. We can accomplish this by applying the query to the ``items_item.name`` column, but we have to make sure that we call `select_related <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#select-related>`_ so the Item table is JOINed and its columns are available in the query.

We cannot use the ``select_related`` trick with ``text_search_part_name`` as it doesn't work with reverse relationships. To get around this, we simply make use of ``PartQueryset``'s ``text_search_name`` with a ``parts__id__in`` lookup, which will be translated to an inner query that does the full text search. Notice that the result of this query might have duplicates, so you might want to add a `distinct <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#distinct>`_ modifier to it.

Full Text Search with MySQL
---------------------------

MySQL introduced `full text search for MyISAM tables in version 5.5 <https://dev.mysql.com/doc/refman/5.5/en/fulltext-search.html>`_. Subsequent versions allow `full text search with InnoDB <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search.html>`_ tables as well. Full text search are performed using the `MATCH <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search.html#function_match>`_ function:

::

    mysql> SELECT * FROM articles
        WHERE MATCH (title,body)
        AGAINST ('database' IN NATURAL LANGUAGE MODE);
    +----+-------------------+------------------------------------------+
    | id | title             | body                                     |
    +----+-------------------+------------------------------------------+
    |  1 | MySQL Tutorial    | DBMS stands for DataBase ...             |
    |  5 | MySQL vs. YourSQL | In the following database comparison ... |
    +----+-------------------+------------------------------------------+
    2 rows in set (0.00 sec)

The query above (taken from MySQL's documentation) looks for 'database' on the 'title' and 'body' columns fo the 'articles' table using full text search. This will only work if the 'article' table has a FULLTEXT index defined against the 'title' and 'body' tables. As with any regular index, it can be defined during the table creation:

::

    CREATE TABLE articles (
        id INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY,
        title VARCHAR(200),
        body TEXT,
        FULLTEXT (title,body)
    ) ENGINE=InnoDB;

or afterwards:

::

    CREATE FULLTEXT INDEX title_body_ft_idx ON articles(title, body);

So, before we can make full text search queries with MySQL with our Django model, we have create these indexes. We'll use a migration for this:

::

    class Migration(migrations.Migration):

        dependencies = [
            ('items', '0001_initial'),
        ]

        operations = [
            migrations.RunSQL(
                'CREATE FULLTEXT INDEX items_item_name_ts_idx ON items_item(name);',
                'ALTER TABLE items_item DROP INDEX items_item_name_ts_idx;',
            ),
            migrations.RunSQL(
                'CREATE FULLTEXT INDEX items_part_name_ts_idx ON items_part(name);',
                'ALTER TABLE items_part DROP INDEX items_part_name_ts_idx;',
            )
        ]

As in the PostgreSQL section, We create two indexes: one for the ``Item``'s name and one for the ``Part``'s name. We can now make full text search queries on the ``name`` field of the ``Item`` and ``Part``. We now can write these queries as ``QuerySet``:

::

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
            return self.filter(parts__id__in=Part.objects.text_search_name(name))


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

Again, we made use of the ``QuerySet`` `extra <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#extra>`_ modifier to express the full text search queries using the MATCH function to exclude rows that doesn't match our query (those with MATCH values equal to 0), and we order the results bases on this value.

The ``text_search_item_name`` and ``text_search_part_name`` shows you how to use the full text search with related tables. In ``text_search_item_name``, we're looking for Part objects whose related Item matches a specific text search query on its name. We can accomplish this by applying the query to the ``items_item.name`` column, but we have to make sure that we call `select_related <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#select-related>`_ so the Item table is JOINed and its columns are available in the query.

We cannot use the ``select_related`` trick with ``text_search_part_name`` as it doesn't work with reverse relationships. To get around this, we simply make use of ``PartQueryset``'s ``text_search_name`` with a ``parts__id__in`` lookup, which will be translated to an inner query that does the full text search. Notice that the result of this query might have duplicates, so you might want to add a `distinct <https://docs.djangoproject.com/en/1.9/ref/models/querysets/#distinct>`_ modifier to it.

Example
-------

Before we show you a sample shell session making the queries, we use the ``QuerySet`` as managers of our models:

::

    class Item(models.Model):
        ...

        objects = ItemQueryset.as_manager()

    class Part(models.Model):
        ...

        objects = PartQueryset.as_manager()

In the following sample shell session you can see how the searches are performed. This works both for PostgreSQL and MySQL:

::

    >>> Item.objects.text_search_name('malesuada')
    [<Item: a, malesuada id, erat. Etiam vestibulum>, <Item: elit, dictum eu, eleifend nec, malesuada ut, sem.>, <Item: blandit. Nam nulla magna, malesuada vel, convallis>, <Item: malesuada fames ac turpis egestas. Aliquam fringilla cursus>]
    >>> Part.objects.text_search_name('zatyPjg')
    [<Part: XlUfMZz zatyPjg jtrJDm sFYXb vdoZx>]
    >>> Item.objects.text_search_part_name('zatyPjg')
    [<Item: elit, dictum eu, eleifend nec, malesuada ut, sem.>]
    >>> Part.objects.text_search_item_name('malesuada')
    [<Part: GHxACaz>, <Part: OhXQwmHx CABsgVDI EKaBA x NFBKOT joDLaM>, <Part: npQAIhf FjacKz hbWDwG IicMPqpK EWYQmj YXz hlUsvjBO>, <Part: XlUfMZz zatyPjg jtrJDm sFYXb vdoZx>, <Part: ls JlNp YDghUXW FpRhxSk>, <Part: Onh ZuESiM M>, <Part: gTJtUC IatOSclg>]
    >>> [part.item for part in Part.objects.text_search_item_name('malesuada')]
    [<Item: a, malesuada id, erat. Etiam vestibulum>, <Item: elit, dictum eu, eleifend nec, malesuada ut, sem.>, <Item: elit, dictum eu, eleifend nec, malesuada ut, sem.>, <Item: elit, dictum eu, eleifend nec, malesuada ut, sem.>, <Item: blandit. Nam nulla magna, malesuada vel, convallis>, <Item: blandit. Nam nulla magna, malesuada vel, convallis>, <Item: malesuada fames ac turpis egestas. Aliquam fringilla cursus>]

Conclusion
----------

As you can see, the solution is pretty much identical in both cases, which suggests that it might possible to adapt it to other database backends with full text search support (as `SQLite <https://sqlite.org/fts5.html>`_). Although I haven't personally tested these solutions with a large site, I found several articles online suggesting that the full text search support for MySQL and PostgreSQL are efficient and reliable.

The code
--------

You can get the for both solutions on `GitHub <https://github.com/abarto/v>`_. The code for each solution is on its own branch:

* `PostgreSQL <https://github.com/abarto/full_text_search_django/tree/full-text-search-postgresql>`_
* `MySQL <https://github.com/abarto/full_text_search_django/tree/full-text-search-mysql>`_

Vagrant
-------

A `Vagrant <https://www.vagrantup.com/>`_ configuration file is included if you want to test the solutions.

Feedback
--------

As usual, I welcome comments, suggestions and pull requests.

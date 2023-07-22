import csv
import pandas as pd
from .models import Product, Category
from django.utils.text import slugify
from decimal import Decimal

#TODO if not category
#TODO sql inj checking


def secure_csv(file_path):
    ...

def procces_csv_categories(file_path):
    tmp_data = pd.read_csv(file_path)
    for row in tmp_data.index:
        category = tmp_data.loc[row, 'category']
        try:
            Category.objects.get(name=category)
        except Category.DoesNotExist:
            Category.objects.create(name=category, slug=slugify(category))

def process_csv(file_path):

    procces_csv_categories(file_path)

    tmp_data = pd.read_csv(file_path, sep=',')

    print(tmp_data.loc[0, 'price'], "TMPMTPTMPT")

    products = [
        Product(
        category=Category.objects.get(name=tmp_data.loc[row, 'category']),
        name=tmp_data.loc[row, 'name'],
        slug=slugify(tmp_data.loc[row, 'name']),
        description=tmp_data.loc[row, 'description'],
        price=Decimal(tmp_data.loc[row, 'price'].item()),
        ) for row in tmp_data.index
    ]

    Product.objects.bulk_create(products)

    print(products)


        # [tmp_data.loc[row, 'category'],
        # tmp_data.loc[row, 'name'],
        # tmp_data.loc[row, 'slug'],
        # tmp_data.loc[row, 'image'],
        # tmp_data.loc[row, 'description'],
        # tmp_data.loc[row, 'price'],
        # tmp_data.loc[row, 'available'] ]
        # for row in tmp_data.index

import csv
import pandas as pd
from .models import Product, Category
from django.utils.text import slugify
from decimal import Decimal

#TODO if not category
#TODO sql inj checking


def secure_csv(file_path):
    ...

INVALID_CHARS = '\'\"+-='

def contains_invalid(strings_array, invalid_chars_string=INVALID_CHARS):
    '''
    ['good', 'good', 'good'] -> False
    ['bad"', 'b"ad'] -> True
    '''
    for string in strings_array:
        if any(invalid_char in string for invalid_char in invalid_chars_string):
            return True
    return False




def procces_csv_categories(file_path):
    tmp_data = pd.read_csv(file_path)
    for row in tmp_data.index:
        category = tmp_data.loc[row, 'category']

        if contains_invalid([category]):
            continue

        try:
            Category.objects.get(name=category)
        except Category.DoesNotExist:
            Category.objects.create(name=category, slug=slugify(category))

def process_csv(file_path, profile_csv_owner):

    procces_csv_categories(file_path)

    tmp_data = pd.read_csv(file_path, sep=',')

    products = []
    exceptions = []

    for row in tmp_data.index:
        category_name = tmp_data.loc[row, 'category']
        name = tmp_data.loc[row, 'name']
        description =tmp_data.loc[row, 'description']
        price = str(tmp_data.loc[row, 'price'])

        if contains_invalid([category_name, name, description]):
            
            exceptions.append(row)
            continue
        
        if not price.isdecimal():
            continue

        products += [Product(
            category=Category.objects.get(name=category_name),
            name=name,
            slug=slugify(name),
            description=description,
            price=Decimal(tmp_data.loc[row, 'price'].item()),
            consumer_profile=profile_csv_owner
        )]
    if exceptions:
        print('Exceptions was added: ', exceptions)

    # products = [
    #     Product(
    #     category=Category.objects.get(name=tmp_data.loc[row, 'category']),
    #     name=tmp_data.loc[row, 'name'],
    #     slug=slugify(tmp_data.loc[row, 'name']),
    #     description=tmp_data.loc[row, 'description'],
    #     price=Decimal(tmp_data.loc[row, 'price'].item()),
    #     ) for row in tmp_data.index
    # ]

    Product.objects.bulk_create(products)

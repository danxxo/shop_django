import csv
import pandas as pd
#from .models import Product


def process_csv(file_path):
    tmp_data = pd.read_csv(file_path, sep=',')


    products = [
        
        [tmp_data.loc[row, 'category'],
        tmp_data.loc[row, 'name'],
        tmp_data.loc[row, 'slug'],
        tmp_data.loc[row, 'image'],
        tmp_data.loc[row, 'description'],
        tmp_data.loc[row, 'price'],
        tmp_data.loc[row, 'available'] ]
        for row in tmp_data.index
    ]
    print(products)

process_csv('/home/shabalka/Desktop/shop/some.csv')
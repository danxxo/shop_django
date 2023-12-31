# Generated by Django 4.1.7 on 2023-07-24 13:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_uploadedcsv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[\'"+-=]', inverse_match=True, message='Avoid quotation and math operators')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, validators=[django.core.validators.RegexValidator('[\'"+-=]', inverse_match=True, message='Avoid quotation and math operators')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('[\'"+-=]', inverse_match=True, message='Avoid quotation and math operators')]),
        ),
    ]

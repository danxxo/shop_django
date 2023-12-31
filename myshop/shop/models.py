from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from account.models import Profile

class Category(models.Model):
    name = models.CharField(max_length=200,
                            validators=[settings.SQL_INJECTION_VALIDATOR])
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        print('save func')
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', 
                                 on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200,
                            validators=[settings.SQL_INJECTION_VALIDATOR])
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True,
                                   validators=[settings.SQL_INJECTION_VALIDATOR])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    consumer_profile = models.ForeignKey(Profile,
                                         on_delete=models.CASCADE,
                                         blank=True,
                                         null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def __str__(self) -> str:
        return self.name
    

class UploadedCSV(models.Model):
    consumer = models.CharField(max_length=30)
    csv = models.FileField(upload_to='upload_csv/%Y/%m/%d')
    



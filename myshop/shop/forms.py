from django import forms
from .models import Category, Product
from django.utils.text import slugify

class ProductCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"

    class Meta:
        model = Product
        fields = [
            'name',
            'image',
            'slug',
            'description',
            'price',
            'category',
            'available'
        ]
    slug = forms.CharField(initial='!default initial slug!')
    
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug or slug == '!default initial slug!':
            name = self.cleaned_data.get('name')
            slug = slugify(name)
        self.cleaned_data['slug'] = slug
        return slug


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug'
        ]

        widgets = {'slug': forms.HiddenInput()}

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug or slug == '!default initial slug!':
            name = self.cleaned_data.get('name')
            slug = slugify(name)
        self.cleaned_data['slug'] = slug
        return slug

    slug = forms.CharField(initial='!default initial slug!')
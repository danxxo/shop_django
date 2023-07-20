from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ProductCreateForm, CategoryCreateForm
from django.utils.text import slugify

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(
            Category, slug=category_slug
        )
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('/')
    else:
        product_form = ProductCreateForm()
    return render(request, 
                  'shop/product/create.html',
                  {'product_form': product_form})

def create_category(request):
    if request.method == 'POST':
        category_form = CategoryCreateForm(request.POST)
        print(category_form.is_valid())
        if category_form.is_valid():
            category_form.save()
            print('POST')
            return redirect('/')
    else:
        category_form = CategoryCreateForm()
        print("GET")
        return render(request,
                      'shop/product/create_category.html',
                      {'category_form': category_form})

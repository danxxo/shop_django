from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Category, Product, UploadedCSV
from cart.forms import CartAddProductForm
from .forms import ProductCreateForm, CategoryCreateForm, UploadCSVForm
from django.utils.text import slugify
from django.conf import settings
from .csv_processing import process_csv
from account.models import Profile
from django.contrib.auth.decorators import login_required
import datetime

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


@login_required    
def create_product(request):
    if request.method == 'POST':
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            print(product_form.cleaned_data)
            product_form.save()
            return redirect('/')
    else:
        user = request.user
        profile = Profile.objects.get(user=user)
        data={'consumer_profile': profile,
              'slug': '!default initial slug!',
              'available': True}
        product_form = ProductCreateForm(data=data)
    return render(request, 
                  'shop/product/create.html',
                  {'product_form': product_form})


@login_required    
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

@login_required    
def upload_csv(request):
    if request.method == 'POST':
        csv_form = UploadCSVForm(request.POST, request.FILES)
        if csv_form.is_valid():
            curr_date_path = datetime.date.today().strftime("/upload_csv/%Y/%m/%d/")
            file_name = str(csv_form.cleaned_data['csv'])
            if not file_name.endswith(".csv"):
                return HttpResponse(f"Uploaded file is not CSV format. Your file: {str(file_name)}")
            csv_form.save()
            file_path = str(settings.MEDIA_ROOT) + curr_date_path + file_name
            profile = Profile.objects.get(user=request.user)
            process_csv(file_path, profile)
            return redirect('/')
    else:
        csv_form = UploadCSVForm(initial={'consumer': str(request.user)})
        return render(request,
                      'shop/product/csv_handler.html',
                      {'csv_form': csv_form})


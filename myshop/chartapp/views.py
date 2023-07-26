from django.shortcuts import render
from shop.models import Category, Product
from account.models import Profile
from orders.models import Order, OrderItem
from django.contrib.admin.views.decorators import staff_member_required
from .forms import DateForm

from .chartapp import get_top_products, get_users_vs_consumers, get_category_amount


@staff_member_required
def index(request):

    category_amount = get_category_amount()

    users_count = get_users_vs_consumers()
            
    if request.method == 'POST':
        dateform = DateForm(request.POST)
        start = request.POST.get('start')
        end = request.POST.get('end')
        choice = request.POST.get('choice')
        
        
        top_products = get_top_products(start, end, choice)

    else:
        top_products = get_top_products(None, None, 4)
        dateform = DateForm()
    
    data = {'categories': category_amount,
            'users_count': users_count,
            'top_products': top_products,
            'form': dateform}

    return render(request,
                  'charts/main.html',
                  data)

from django.shortcuts import render
from shop.models import Category, Product
from account.models import Profile
from orders.models import Order, OrderItem
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
def index(request):

    categry_amount = {}

    categories = list(Category.objects.all())
    for cat in categories:
        categry_amount[cat] = Product.objects.filter(category=cat).count()

    all_users_count = Profile.objects.all().count()
    consumers_users_count = Profile.objects.filter(is_consumer=True).count()
    sellers_users_count = all_users_count - consumers_users_count

    users_count = {
        'consumers': consumers_users_count,
        'sellers': sellers_users_count
    }

    # Top products according to orders
    all_orders = Order.objects.all()
    top_products = {}
    for order in all_orders:
        order_items = OrderItem.objects.filter(order=order)
        for order_item in order_items:
            if order_item.product.name not in top_products:
                top_products[order_item.product.name] = order_item.quantity
            else:
                top_products[order_item.product.name] += order_item.quantity
    
    data = {'categories': categry_amount,
            'users_count': users_count,
            'top_products': top_products}

    return render(request,
                  'charts/main.html',
                  data)

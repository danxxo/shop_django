from orders.models import Order, OrderItem
from shop.models import Product, Category
from account.models import Profile
import datetime
from django.utils import timezone
from django.forms import ValidationError

tz = timezone.now()

def get_top_products(start, end, choice):

    choice = int(choice)

    top_products = {}
    all_orders = []
    
    if choice != 0:
        if choice == 1:

            end = datetime.date.today()
            start = end - datetime.timedelta(days=7)
            all_orders = Order.objects.filter(created__range=[start, end])

        if choice == 2:

            end = datetime.date.today()
            start = end - datetime.timedelta(days=30)
            all_orders = Order.objects.filter(created__range=[start, end])

        if choice == 3:

            end = datetime.date.today()
            start = end - datetime.timedelta(days=365)
            all_orders = Order.objects.filter(created__range=[start, end])

        if choice == 4:
            all_orders = Order.objects.all()
        
    else:
        if  start and  end:
            all_orders = Order.objects.filter(created__range=[start, end])
            
        else:
            all_orders = Order.objects.all()

    for order in all_orders:
        order_items = OrderItem.objects.filter(order=order)

        for order_item in order_items:
            if order_item.product.name not in top_products:
                top_products[order_item.product.name] = order_item.quantity
            else:
                top_products[order_item.product.name] += order_item.quantity
    return top_products


def get_users_vs_consumers():
    all_users_count = Profile.objects.all().count()
    consumers_users_count = Profile.objects.filter(is_consumer=True).count()
    sellers_users_count = all_users_count - consumers_users_count

    users_count = {
        'consumers': consumers_users_count,
        'sellers': sellers_users_count
    }

    return users_count

def get_category_amount():
    category_amount = {}

    categories = list(Category.objects.all())
    for cat in categories:
        category_amount[cat] = Product.objects.filter(category=cat).count()
    
    return category_amount 
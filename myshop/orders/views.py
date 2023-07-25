from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from account.models import Profile
from django.contrib.auth.models import User


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print('smvornvoinpn')
        print(form.is_valid())
        print(form.fields['username'])
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
        else:
            print(form.errors)
    else:
        user = request.user
        profile = Profile.objects.get(user=user)
        data = {'username': profile,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email}
        form = OrderCreateForm(data=data)
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})
    

@login_required
def my_orders(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    orders = Order.objects.filter(username=profile)
    orders_to_post = {}
    for order in orders:
        orders_to_post[order] = list(OrderItem.objects.filter(order=order))
    
    
    print(user)
    return render(request,
                  'orders/order/my_orders.html',
                  {'orders': orders_to_post})

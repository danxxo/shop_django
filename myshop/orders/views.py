from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
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
        user = request.user
        print(user.username)
        data = {'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email}
        form = OrderCreateForm(data=data)
        return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form})
    

@login_required
def my_orders(request):
    ...

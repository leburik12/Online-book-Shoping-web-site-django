from django.shortcuts import render
from book.models import Books
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from decimal import Decimal


def checkout_order(request):
    cart = Cart(request)

    form = OrderCreateForm()
    if request.method == 'POST':
        form  = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         new_book_paperback_price=Decimal(item['new_book_paperback_price']),
                                         new_book_hardcover_price=Decimal(item['new_book_hardcover_price']),
                                         old_book_hardcover_price=Decimal(item['old_book_hardcover_price']),
                                         new_book_hardcover_qty=int(item['new_book_qty']),
                                         new_book_paperback_qty=int(item['paper_back_qty']),
                                         old_book_hardcover_qty=int(item['used_book_qty']))
            # Clear the cart
            cart.clear()
            return render(request, 'orders/orders_created.html', {'order': order})
    return render(request, 'orders/checkout.html', {'cart': cart,'form': form})
    # if request.method == 'POST':
    #     form = OrderCreateForm(request.POST)
    #     if form.is_valid():
    #         order = form.save()






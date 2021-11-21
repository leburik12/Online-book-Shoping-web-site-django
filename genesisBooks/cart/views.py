from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from book.models import Books
from .cart import Cart
from .forms import AddToCartForm
from django.http import JsonResponse
import re


@require_POST
def cart_add(request, book_id):
     cart = Cart(request)
     book = get_object_or_404(Books, pk=book_id)
     form = request.POST
     if 'hardcover_qty' in form.keys():
         new_book_quantity = (form['hardcover_qty'] if int( form['hardcover_qty'] ) != 0 else 0)
         new_book_quantity = re.sub( '[^0-9]', "-", str( new_book_quantity ) )
     else:
         new_book_quantity = 0
     if 'paperback_qty' in form.keys():
         paper_back_quantity = (form['paperback_qty'] if int( form['paperback_qty'] ) != 0 else 0)
         paper_back_quantity = re.sub( '[^0-9]', "-", str( paper_back_quantity ) )
     else:
          paper_back_quantity = 0
     if 'usedhardcover_qty' in form.keys():
         old_book_quantity = (form['usedhardcover_qty'] if int( form['usedhardcover_qty'] ) != 0 else 0)
         old_book_quantity = re.sub( '[^0-9]', "-", str( old_book_quantity ) )
     else:
          old_book_quantity = 0
     override = form['override']
     cart.add(book=book,new_book_qty=int(new_book_quantity),
                    used_book_qty=int(old_book_quantity),override_quantity=override,
              paperback_qty=int(paper_back_quantity))
     return redirect('cart:cart_detail')

@require_POST
def cart_remove(request):
     book_id = request.POST.get('book_id')
     cart = Cart( request )
     # book = get_object_or_404(Books, id=book_id)
     cart_response = cart.remove(str(book_id))
     return JsonResponse({'message': 'ok', 'status': 200, 'cart_content': cart_response})

def cart_detail(request):
     cart = Cart(request)
     # for my in cart:
     #      print('Got the item in the extra')
          # item_qtys = cart[str(item['book_id'])]
          # item['update_quantity_form'] = AddToCartForm(initial={
          #      'new_book_quantity': item_qtys['new_book_qty'],
          #      'old_book_quantity': item_qtys['used_book_qty'],
          #      'paper_back_quantity': item_qtys['paper_back_qty'],
          #      'override': True,
          # })
     return render(request, 'cart/cart_detail.html', {'cart': cart})

from decimal import Decimal
from django.conf import settings
from book.models import Books
from django.db.models import Count, F


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:  # if no cart is yet added
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book, new_book_qty = 0, used_book_qty = 0, override_quantity=False, paperback_qty = 0):
        """
        Add a product to the cart or update its quantity
        """
        book_id = str(book.id)
        book_data = Books.objects.filter(pk=book_id).values('new_book_hardcover_price','old_book_hardcover_price','new_book_paperback_price',
                                'new_book_hardcover_qty','new_book_paperback_qty','old_book_hardcover_qty')
        if book_id not in self.cart:
            self.cart[book_id] = {'new_book_qty': new_book_qty,
                                  'used_book_qty': used_book_qty,
                                  'paper_back_qty': paperback_qty,
                                  'new_book_hardcover_price': str(book_data[0]['new_book_hardcover_price']),
                                  'old_book_hardcover_price': str(book_data[0]['old_book_hardcover_price']),
                                  'new_book_paperback_price': str(book_data[0]['new_book_paperback_price']),
                                  'total_qty': new_book_qty + used_book_qty + paperback_qty,
                                  'total_price': str((new_book_qty * book_data[0]['new_book_hardcover_price']) +
                                                 (used_book_qty * book_data[0]['old_book_hardcover_price']) +
                                                 (paperback_qty * book_data[0]['new_book_paperback_price']))
            }
            # Books.objects.filter(pk=book_id).update(new_book_hardcover_qty=F('new_book_hardcover_qty') - new_book_qty,
            #             old_book_hardcover_qty=F('old_book_hardcover_qty') - used_book_qty,
            #             new_book_paperback_qty=F('new_book_paperback_qty') - paperback_qty)

            # book.update(new_book_hardcover_qty=book.new_book_hardcover_price-1,)
            self.save()
            return
        if override_quantity:
            self.cart[book_id]['new_book_qty'] = new_book_qty
            self.cart[book_id]['used_book_qty'] = used_book_qty
            self.cart[book_id]['paper_back_qty'] = paperback_qty
            self.cart[book_id]['total_qty'] += new_book_qty + used_book_qty + paperback_qty
            self.cart[book_id]['total_price'] = str(((self.cart[book_id]['new_book_qty']) * (Decimal(self.cart[book_id]['new_book_hardcover_price'])))  \
                                  + ((self.cart[book_id]['used_book_qty']) * (Decimal(self.cart[book_id]['old_book_hardcover_price']))) \
                                  + ((self.cart[book_id]['paper_back_qty']) * (Decimal(self.cart[book_id]['new_book_paperback_price']))))
            # Books.objects.filter( pk=book_id ).update(
            #     new_book_hardcover_qty=F( 'new_book_hardcover_qty' ) - new_book_qty,
            #     old_book_hardcover_qty=F( 'old_book_hardcover_qty' ) - used_book_qty,
            #     new_book_paperback_qty=F( 'new_book_paperback_qty' ) - paperback_qty )
        else:
            # print( '**************************************')
            # print(f"cart new_book_qty --- ${self.cart[book_id]['new_book_qty']}")
            # print(new_book_qty)
            self.cart[book_id]['new_book_qty'] += new_book_qty
            self.cart[book_id]['used_book_qty'] += used_book_qty
            self.cart[book_id]['paper_back_qty'] += paperback_qty
            self.cart[book_id]['total_qty'] += new_book_qty + used_book_qty + paperback_qty
            self.cart[book_id]['total_price'] = str(
                ((self.cart[book_id]['new_book_qty']) * (Decimal( self.cart[book_id]['new_book_hardcover_price'] ))) \
                + ((self.cart[book_id]['used_book_qty']) * (Decimal( self.cart[book_id]['old_book_hardcover_price'] ))) \
                + ((self.cart[book_id]['paper_back_qty']) * (
                    Decimal( self.cart[book_id]['new_book_paperback_price'] ))) )
            # Books.objects.filter( pk=book_id ).update(
            #     new_book_hardcover_qty=F( 'new_book_hardcover_qty' ) - new_book_qty,
            #     old_book_hardcover_qty=F( 'old_book_hardcover_qty' ) - used_book_qty,
            #     new_book_paperback_qty=F( 'new_book_paperback_qty' ) - paperback_qty )
        self.save()

    def save(self):
        # mark the session as 'modified' to make sure it gets saved
        self.session.modified = True

    def remove(self, book_id):
        """
        Remove a product from the cart
        """
        removed_amount = 0
        removed_qty = 0

        book__id = str(book_id)
        if book__id in self.cart:
            removed_qty = self.cart[book_id]['total_qty']
            removed_amount = self.cart[book_id]['total_price']
            del self.cart[book__id]
            self.get_total_price()  # update the total price
            self.save()
            return {
                "removed_qty": removed_qty,
                "removed_amount": removed_amount,
            }
    def __getitem__(self, index):
        item = {}
        item['new_book_qty'] = self.cart[index]['new_book_qty']
        item['used_book_qty'] = self.cart[index]['used_book_qty']
        item['paper_back_qty'] = self.cart[index]['paper_back_qty']
        return

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database
        """
        book_ids = self.cart.keys()
        # get the product objects and add them to the cart
        books = Books.objects.filter(id__in=book_ids)

        cart = self.cart.copy()  # we copied the cart to new cart
        for book in books:
            cart[str(book.id)]['book'] = book
            cart[str(book.id)]['book_id'] = book.id

        for item in cart.values():
            item['new_book_hardcover_price'] = Decimal(item['new_book_hardcover_price'])
            item['old_book_hardcover_price'] = Decimal(item['old_book_hardcover_price'])
            item['new_book_paperback_price'] = Decimal(item['new_book_paperback_price'])
            item['new_book_total'] = Decimal(item['new_book_hardcover_price']) * int(item['new_book_qty'])
            item['used_book_total'] = Decimal( item['old_book_hardcover_price'] ) * int( item['used_book_qty'] )
            item['paper_back_total'] = Decimal( item['new_book_paperback_price'] ) * int( item['paper_back_qty'] )
            item['total_price'] = item['total_price']
            item['book_id'] = item['book_id']
            # item['total_price'] = (item['new_book_qty'] * item['new_book_hardcover_price'])  \
            #                       + (item['used_book_qty'] * item['old_book_hardcover_price']) \
            #                       + (item['paper_back_qty'] * item['new_book_paperback_price'])
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['total_qty'] for item in self.cart.values())

    def get_total_price(self):
        sum = 0
        for item in self.cart.values():
            price = item['total_price'].split('.')[:2]
            price = Decimal(price[0]+'.'+price[1])
            sum += price
        return sum
        # return sum(Decimal(item['total_price']) for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()



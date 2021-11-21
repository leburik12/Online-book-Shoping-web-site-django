from django import forms
from book.models import Books
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(0, 21)]

class AddToCartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        book_id = kwargs.pop('data').get('pk')
        super( AddToCartForm, self ).__init__( *args, **kwargs )
        self.book_qtys = Books.availablebook.filter( id=book_id ).values_list(
            'new_book_hardcover_qty',
            'old_book_hardcover_qty' ,
        'new_book_paperback_qty')
        if self.book_qtys[0][0] != 0:  # check if new_book_hardcover_qty is not zero
            self.fields['new_book_quantity'] = forms.IntegerField( max_value=self.book_qtys[0][0], required=False,initial=1 )
        if self.book_qtys[0][1] != 0:
            self.fields['old_book_quantity'] = forms.IntegerField( max_value=self.book_qtys[0][1], required=False,initial=0 )
        if self.book_qtys[0][2] != 0:
            self.fields['paper_back_quantity'] = forms.IntegerField( max_value=self.book_qtys[0][1], required=False,initial=0 )
    coupon = forms.CharField( max_length=100, required=False )
    override = forms.BooleanField(required=False,
                                  initial=False,widget=forms.HiddenInput)
    bk_id = forms.IntegerField(required=True, widget=forms.HiddenInput)
    # def clean(self):
    #     super().clean()
    #     bookid = self.cleaned_data.get('bk_id')
    #     book = Books.objects.filter(pk=bookid).values('new_book_paperback_qty','new_book_paperback_qty','new_book_hardcover_qty','coupon').get(pk=bookid)
    #     new_book_quantity = self.cleaned_data.get('new_book_quantity')
    #     paperback_book_quantity = self.cleaned_data.get( 'paper_back_quantity')
    #     old_book_quantity = self.cleaned_data.get('old_book_quantity')
    #     book_coupon = self.cleaned_data.get('coupon')
    #     if book_coupon:
    #         if book_coupon.lower() != book['coupon'].lower():
    #             raise ValidationError(f"Sorry there is no coupon name called {self.book['old_book_hardcover_qty']}.Contact Service for help")
    #     if old_book_quantity > book['new_book_paperback_qty']:
    #         raise ValidationError(f"Sorry We only got {self.book['old_book_hardcover_qty']}.Contact Service for help")
    #     if paperback_book_quantity > book['new_book_paperback_qty']:
    #         raise ValidationError(
    #             f"Sorry We only got {self.book['new_book_paperback_qty']} for PaperBack format.Contact Service for help" )
    #     if new_book_quantity > book['new_book_hardcover_qty']:
    #         raise ValidationError(f"Sorry We only got {book['new_book_hardcover_qty']} for HardCover format.Contact Service for help")
    #

    # def book_returner(self):
    #     bookid = self.cleaned_data.get('bk_id')
    #     test = self.cleaned_data.get('csrfmiddlewaretoken')
    #     print(test)
    #     print(bookid)
    #     print( '(((((((((((((((((((((((((((((((((((((((((((((((((((((((')
    #     book = Books.objects.get(id=bookid).select_related('new_book_hardcover_qty','new_book_paperback_qty','old_book_hardcover_qty','coupon')
    #     print(book)
    #
    #     return book
    #
    # def clean_new_book_quantity(self):
    #     book = self.book_returner()
    #     new_book_quantity = self.cleaned_data.get('new_book_quantity')
    #     if new_book_quantity > book['new_book_hardcover_qty']:
    #         raise ValidationError(f"Sorry We only got {self.book['new_book_hardcover_qty']} for HardCover format.Contact Service for help")
    #     return self.new_book_quantity
    #
    # def clean_paper_back_quantity(self):
    #     book = self.book_returner()
    #     paperback_book_quantity = self.cleaned_data.get('paper_back_quantity')
    #     if paperback_book_quantity > book['new_book_paperback_qty']:
    #         raise ValidationError(f"Sorry We only got {self.book['new_book_paperback_qty']} for PaperBack format.Contact Service for help")
    #     return self.paper_back_quantity
    #
    # def clean_old_book_quantity(self):
    #     book = self.book_returner()
    #     old_book_quantity = self.cleaned_data.get('old_book_quantity')
    #     if old_book_quantity > book['new_book_paperback_qty']:
    #         raise ValidationError(f"Sorry We only got {self.book['old_book_hardcover_qty']}.Contact Service for help")
    #     return self.old_book_quantity
    #
    # def clean_coupon(self):
    #     book = self.book_returner()
    #     book_coupon = self.cleaned_data.get('coupon')
    #     if book_coupon.lower() != book['coupon'].lower():
    #         raise ValidationError(f"Sorry there is no coupon name called {self.book['old_book_hardcover_qty']}.Contact Service for help")
    #     return self.coupon

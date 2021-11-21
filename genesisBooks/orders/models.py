from django.db import models
from book.models import Books
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100)
    phone_number_1 = models.PositiveIntegerField()
    phone_number_2 = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    book = models.ForeignKey(Books,
                             related_name='ordered_book',
                             on_delete=models.CASCADE)
    new_book_paperback_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_book_hardcover_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    old_book_hardcover_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    new_book_hardcover_qty = models.PositiveIntegerField()
    new_book_paperback_qty = models.PositiveIntegerField()
    old_book_hardcover_qty = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        price = (self.new_book_hardcover_price +
                self.new_book_paperback_price +
                self.old_book_hardcover_price )
        quantity = (self.new_book_hardcover_qty +
                         self.new_book_paperback_qty +
                         self.old_book_hardcover_qty)
        return price * quantity






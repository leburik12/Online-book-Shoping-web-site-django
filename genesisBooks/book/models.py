from django.db import models
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from account.models import Customer


class AvailableBooksManager(models.Manager):
    def get_queryset(self):
        return super(AvailableBooksManager, self).get_queryset().filter(no_more_book=False)

class Books(models.Model):

    CATEGORY_CHOICES = [
        ('arts & philosophy', 'Arts'),
        ('biographies & memories', 'Biographies & Memories'),
        ('business & Money', 'Business & Money'),
        ('calendar', 'Calendar'),
        ('children books', 'Children\'s Books'),
        ('christian books & Bibles', 'Christian Books & Bibles'),
        ('comics & graphic novels', 'Comics & Graphic Novels'),
        ('computer & technology', 'Computer & Technology'),
        ('Cookbooks, Food & Wine', 'Cookbooks, Food & Wine'),
        ('History', 'History'),
        ('Law', 'Law'),
        ('Literature & Fiction', 'Literature & Fiction'),
        ('Medical Books', 'Medical Books'),
        ('Romance', 'Romance'),
        ('Science & Math', 'Science & Math'),
        ('Sport & Outdoors', 'Sport & Outdoors'),
        ('Test preparation', 'Test preparation'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_hardcover = models.BooleanField(default=True)
    is_paperback = models.BooleanField(default=False, blank=True)
    page = models.PositiveIntegerField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    audio_included = models.BooleanField(default=False, blank=True)
    book_image = models.ImageField(upload_to='book_images/%Y/%m/%d/',
                                   blank=True)
    category = models.CharField(max_length=250,
                                choices=CATEGORY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    coupon = models.TextField(blank=True)
    slug = models.SlugField()
    premium_service = models.BooleanField(default=False, blank=True)
    new_book_hardcover_qty = models.PositiveIntegerField(default=1)
    new_book_paperback_qty = models.PositiveIntegerField(blank=True, default=0)
    new_book_hardcover_price = models.DecimalField(max_digits=12, decimal_places=2, default=None)
    new_book_paperback_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0.00)
    old_book_hardcover_qty = models.PositiveIntegerField(default=0, blank=True)
    old_book_paperback_qty = models.PositiveIntegerField(blank=True, default=0)
    old_book_hardcover_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, default=0.0)
    old_book_paperback_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, default=0.0)
    best_seller = models.PositiveIntegerField(null=True, default=0)
    audio_book_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.0)
    audio_book_quantity = models.PositiveIntegerField(blank=True, null=True, default=0.0)
    item_sold = models.PositiveIntegerField(default=0, null=True)
    no_more_book = models.BooleanField(default=False, null=True)
    # raters = models.ManyToManyField(Customer,
    #                                 models.ManyToManyField,
    #
    #                                 blank=True)

    objects = models.Manager()  # default Manage
    availablebook = AvailableBooksManager()  # our custom manager

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('books:book_detail_page', args=[self.slug,
                                                       self.pk
                                                       ])

    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_queryset(self):
        return

# class PremiumService(models.Model):
#     deal_in_days = models.PositiveIntegerField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     book_id = models.ForeignKey('Books',
#                                 on_delete=models.CASCADE,2
#                                 related_name='premium_serviced')

# class Advertisement(models.Model):
#     name = models.CharField(max_length=250, blank=True)
#     body = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class AdContent(models.Model):
#     ad_name = models.ForeignKey('Advertisement',
#                                 on_delete=models.CASCADE,
#                                 related_name='advertisement_content')
#     body = models.TextField()
#     video_url = models.URLField()
#     ad_file = models.FileField(upload_to=f'advertisement_files/{ad_name}/{id}')
#
#
# class AdContent(models.Model):
#     ad_name = models.ForeignKey('Advertisement',
#                                 on_delete=models.CASCADE,
#                                 related_name='ad_contents')
#     content_type = models.ForeignKey(ContentType,
#                                      on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type', 'object_id')

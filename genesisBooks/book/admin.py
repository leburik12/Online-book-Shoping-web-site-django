from django.contrib import admin
from . import models


# class AdContentInline(admin.StackedInline):
#     model = models.AdContent
#     extra = 2


@admin.register(models.Books)
class BookAdmin(admin.ModelAdmin):
    # list_display =
    readonly_fields = ['created',
                       'updated']
    list_filter = ['author', 'is_hardcover', 'is_paperback','rating','category','old_book_hardcover_qty', 'new_book_hardcover_qty']
    prepopulated_fields = {'slug': ('title', 'author')}
    search_fields = ('title', 'author')

from django.urls import path, re_path
from .views import BookLists, BookDetailPage, books_total_list_view, search_books

app_name = 'books'

urlpatterns = [
    path('<slug:slug>/<int:pk>/', BookDetailPage.as_view(), name='book_detail_page'),
    path('category/<str:category>/', books_total_list_view, name='catg_books_total_page'),
    path('condition/<str:condition>/', books_total_list_view, name='condition_books_total_page'),
    path('author/<str:author>/', books_total_list_view, name='books_by_author'),
    path('<str:best_seller>/', books_total_list_view, name='books_by_best_seller'),
    path('<str:all_book>/', books_total_list_view, name='all_books'),
    path('search/', search_books, name='search_books'),
    path('', books_total_list_view, name='books_total_page'),
]


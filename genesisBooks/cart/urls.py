from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:book_id>/', views.cart_add, name='cart_add'),
    path('remove/', views.cart_remove, name='cart_remove'),
]
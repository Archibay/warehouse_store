from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.get_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    # path('cart/', views.CartDetailView.as_view(), name='cart'),
]

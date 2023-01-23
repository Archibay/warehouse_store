from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list')
]

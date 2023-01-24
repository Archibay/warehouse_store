from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Order, OrderItem
from django.contrib.auth.models import User
# from .forms import PostForm, CommentForm, ContactUsForm
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.contrib import messages
# from .tasks import send_mail as celery_send_mail
from django.template.loader import render_to_string
from django.http import JsonResponse


class BookListView(ListView):
    model = Book
    fields = ['title', 'price']
    paginate_by = 10
    template_name = 'store/book_list.html'

    def get_object(self, **kwargs):
        user = self.request.user
        return user


class BookDetailView(DetailView):
    model = Book
    template_name = 'store/book_detail.html'


# @login_required
# def create_order(request):
#     order = Order.objects.get_or_create(user_id=request.user, status='IP')
#     return request


@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk=pk)
    order, create = Order.objects.get_or_create(user_id=request.user, status='IP')
    cart, create = OrderItem.objects.get_or_create(order_id=order, book_id=book)
    cart.quantity += 1
    cart.save()
    # messages.success(request, "Cart updated!")
    return redirect('store:book_detail', pk=book.id)


class CartDetailView(LoginRequiredMixin, DetailView):
    model = OrderItem
    template_name = 'store/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CartDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        context['order_items'] = user.order_set
        context['books'] = user.order_set.ordetitem_set.book.all()
        return context

    def get_object(self, **kwargs):
        user = self.request.user
        return user

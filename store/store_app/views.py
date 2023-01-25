from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Order, OrderItem
from django.contrib.auth.models import User
from .forms import OrderForm
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
from django.core.exceptions import ObjectDoesNotExist


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

def get_cart(request):
    user = request.user
    try:
        order = Order.objects.get(user_id=user.id)
        order_item = OrderItem.objects.filter(order_id=order).all()
        for i in order_item:
            total_price = i.quantity * i.book_id.price
        return render(request, 'store/cart_detail.html', {'total_price': total_price, 'order_item': order_item})
    except ObjectDoesNotExist:
        return render(request, 'store/cart_empty.html')

@login_required
def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():

            return redirect('store:book_list')
    else:
        data = {
            'firs_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        }
        form = OrderForm(data)
    return render(request, 'store/checkout.html', {'form': form})

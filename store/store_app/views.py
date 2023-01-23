from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Order, OrderItem
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


from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    id_in_store = models.IntegerField()


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    IN_PROCESS = 'IP'
    SUCCESS = 'SC'
    FAILED = 'FD'
    STATUS_CHOICES = [
        (IN_PROCESS, 'In process'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed')
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=IN_PROCESS)
    delivery_address = models.CharField(max_length=300)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class BookItem(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    cell = models.CharField(max_length=100)


class Order(models.Model):
    IN_PROCESS = 'IP'
    SUCCESS = 'SC'
    FAILED = 'FD'
    STATUS_CHOICES = [
        (IN_PROCESS, 'In process'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed')
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=IN_PROCESS)
    user_email = models.EmailField(max_length=200)
    delivery_address = models.CharField(max_length=300)
    order_id_in_shop = models.IntegerField()


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_store_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class OrderItemBookItem(models.Model):
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    book_item_id = models.ManyToManyField(BookItem)

from django.core.management.base import BaseCommand
from warehouse_app.models import Book, BookItem
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Fill db'

    def add_arguments(self, parser):
        parser.add_argument('total_b', type=int, choices=range(0, 1001), help='Numbers of Books')

    def handle(self, **kwargs):
        # add Books
        total_b = kwargs['total_b']
        Book.objects.bulk_create(
            [Book(title=fake.sentence(nb_words=random.randrange(1, 5)),
                  price=random.randrange(200, 1000, 10))
             for i in range(total_b)]
        )

        # add Books items
        b_list = Book.objects.values_list('id', flat=True)
        for i in range(total_b):
            random_b = random.choice(b_list)
            objs = BookItem(book_id=Book.objects.get(id=random_b),
                            cell=random.randrange(1, 20))
            objs.save()

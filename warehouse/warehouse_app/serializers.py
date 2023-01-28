# from rest_framework import serializers
# from warehouse.warehouse_app.models import Book, BookItem
#
#
# class BookSerializer(serializers.ModelSerializer):
#     order_item = BookItemSerializer(many=True, write_only=True)
#
#     class Meta:
#         model = Book
#         fields = '__all__'
#
#
# class BookItemSerializer(serializers.ModelSerializer):
#     order_item = BookItemItemSerializer(many=True, write_only=True)
#
#     class Meta:
#         model = Book
#         fields = '__all__'

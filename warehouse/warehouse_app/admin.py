from django.contrib import admin
from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem


class BookItemInlineModelAdmin(admin.TabularInline):
    model = BookItem
    fk_name = 'book_id'


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['price']
    search_fields = ['title']
    # date_hierarchy = 'created_date'
    list_per_page = 20
    fieldsets = (
        ('Book info', {
            'fields': ('title', 'price')
        }),
    )
    inlines = [BookItemInlineModelAdmin]
    save_as = True


class OrderItemInLineModelAdmin(admin.TabularInline):
    model = OrderItem
    fk_name = 'order_id'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'user_email']
    list_filter = ['status']
    search_fields = ['user_email']
    # date_hierarchy = 'created_date'
    list_per_page = 20
    fieldsets = (
        ('Order info', {
            'fields': ('status', 'user_email', 'delivery_address', 'order_id_in_shop')
        }),
        # ('Client info', {
        #     'fields': ('',)
        # }),
    )
    inlines = [OrderItemInLineModelAdmin]
    save_as = True


admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)

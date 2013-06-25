#coding: utf-8

from django.contrib import admin
import locale

from restaurantsystem.models import Employee, Item, Supplier, Order, MenuItem, OrderMenuItem

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'gender', 'salary', 'admission_date', 'phone_number', 'is_administrative')
    search_fields = list_display
    list_filter = list_display
    date_hierarchy = 'admission_date'
    ordering = ('-admission_date',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit', 'brand')
    exclude = ('quantity',)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number','get_items')
    search_fields = ('name', 'address', 'phone_number','items__name')
    list_filter = ('name', 'address', 'phone_number',)
    filter_horizontal = ('items', )

    def get_items(self, supplier):
        return "<ul><li>"+"</li><li>".join((i.name for i in supplier.items.all()))+"</ul>"

    get_items.allow_tags = True
    get_items.short_description = "Items Fornecidos"

class OrderAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'date', 'get_employee_name')
    search_fields = list_display
    list_filter = ('invoice_number', 'date', 'employee__name')

    def get_employee_name(self, order):
        return order.employee.name

    get_employee_name.short_description = (u'Funcionário')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = list_display
    list_filter = list_display

class OrderMenuItemAdmin(admin.ModelAdmin):

    locale.setlocale(locale.LC_ALL, 'ptb')

    list_display = ('get_order_invoice', 'get_menu_item_name', 'quantity', 'get_unit_price', 'get_partial')
    search_fields = list_display
    list_filter = ('order__invoice_number', 'menu_item__name', 'quantity', 'unit_price')

    def get_order_invoice(self, order_menu_item):
        return order_menu_item.order.invoice_number

    def get_menu_item_name(self, order_menu_item):
        return order_menu_item.menu_item.name

    def get_unit_price(self, order_menu_item):
        return locale.currency(order_menu_item.unit_price)

    def get_partial(self, order_menu_item):
        return locale.currency(order_menu_item.quantity * order_menu_item.unit_price)

    get_order_invoice.short_description = (u'Número do Pedido')
    get_menu_item_name.short_description = (u'Item do Menu')
    get_partial.short_description = (u'Subtotal')
    get_unit_price.short_description = (u'Preço Unitário')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(OrderMenuItem, OrderMenuItemAdmin)

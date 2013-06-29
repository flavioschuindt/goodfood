#coding: utf-8

from django.contrib import admin
import locale

from restaurantsystem.models import Employee, Item, Supplier, \
                                    Order, Product, OrderProduct, \
                                    Purchase, PurchaseItem

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

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = list_display
    list_filter = list_display

class OrderProductAdmin(admin.ModelAdmin):

    locale.setlocale(locale.LC_ALL, 'ptb')

    list_display = ('get_order_invoice', 'get_product_name', 'quantity', 'get_unit_price', 'get_partial')
    search_fields = list_display
    list_filter = ('order__invoice_number', 'product__name', 'quantity', 'unit_price')

    def get_order_invoice(self, order_menu_item):
        return order_menu_item.order.invoice_number

    def get_product_name(self, order_menu_item):
        return order_menu_item.product.name

    def get_unit_price(self, order_menu_item):
        return locale.currency(order_menu_item.unit_price)

    def get_partial(self, order_menu_item):
        return locale.currency(order_menu_item.quantity * order_menu_item.unit_price)

    get_order_invoice.short_description = (u'Número do Pedido')
    get_product_name.short_description = (u'Produto')
    get_partial.short_description = (u'Subtotal')
    get_unit_price.short_description = (u'Preço Unitário')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'date', 'get_employee_name')
    search_fields = list_display
    list_filter = ('invoice_number', 'date', 'employee__name')

    def get_employee_name(self, order):
        return order.employee.name

    get_employee_name.short_description = (u'Funcionário')

class PurchaseItemAdmin(admin.ModelAdmin):

    locale.setlocale(locale.LC_ALL, 'ptb')

    list_display = ('get_purchase_invoice', 'get_product_name', 'quantity', 'get_unit_price', 'get_partial')
    search_fields = list_display
    list_filter = ('purchase__invoice_number', 'item__name', 'quantity', 'unit_price')

    def get_purchase_invoice(self, purchase_item):
        return purchase_item.purchase.invoice_number

    def get_product_name(self, purchase_item):
        return purchase_item.item.name

    def get_unit_price(self, purchase_item):
        return locale.currency(purchase_item.unit_price)

    def get_partial(self, purchase_item):
        return locale.currency(purchase_item.quantity * purchase_item.unit_price)

    get_purchase_invoice.short_description = (u'Número da Compra')
    get_product_name.short_description = (u'Produto')
    get_partial.short_description = (u'Subtotal')
    get_unit_price.short_description = (u'Preço Unitário')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)

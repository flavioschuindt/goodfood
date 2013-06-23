from django.contrib import admin
from restaurantsystem.models import Employee, Item, Supplier

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

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Supplier, SupplierAdmin)

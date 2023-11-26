# admin.py

from django.contrib import admin
from .models import Table_1


class Table_1Admin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'price')  # Отображаемые поля в списке
    list_display_links = ('name', 'unit', 'price')
    search_fields = ('name',)  # Поля для поиска


admin.site.register(Table_1, Table_1Admin)

from django.contrib import admin

# Register your models here.
from main.models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'image', 'time_created', 'category', 'complete')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('complete',)
    list_filter = ('complete', 'time_created')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)

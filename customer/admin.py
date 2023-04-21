from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    fields = ["name", "age", "note", "email", "is_active"] # Fields to use for add/edit/show page
    list_display = ["name", "email"] # fields to display in search page
    list_display_links = ["name"] # fields that will be a link in search page

admin.site.register(Customer, CustomerAdmin)

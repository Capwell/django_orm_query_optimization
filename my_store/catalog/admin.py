from django.contrib import admin

from .models import Category, Item, Tag

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Tag)

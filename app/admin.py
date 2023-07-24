from django.contrib import admin
from app.models import Product, Category, Author, Blog

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Blog)
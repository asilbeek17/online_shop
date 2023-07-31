from django.contrib import admin

from app.models import User, Category, Product, Blog, Feedback

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Feedback)

from django.contrib import admin

from app.models import Category, Product, Blog, User, Feedback, Post

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Feedback)
admin.site.register(Post)
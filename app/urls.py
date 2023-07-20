from django.urls import path

from app.views import index, shop_view, product_detail_view

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop_view, name='shop'),
    path('product-detail/', product_detail_view, name='product-detail'),
]
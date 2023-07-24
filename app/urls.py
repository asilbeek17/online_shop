from django.urls import path
from app.views import index_view, shop_view, product_details_view, product_error404, product_compare_page, \
    product_cart_page, product_checkout_page, product_wishlist_page, product_frequently_questions, product_blog, \
    product_blog_details_page, my_account, login_view, register_page, about_page, contact_page, add_product_view

urlpatterns = [
    path('', index_view, name='index'),
    path('shop-main-page/', shop_view, name='shop_main'),
    path('<int:product_id>/', product_details_view, name='product-details'),
    path('add-product/', add_product_view, name='add-product'),
    path('product-error404-page/', product_error404, name='product-error404'),
    path('product-compare-page/', product_compare_page, name='product-compare-page'),
    path('product-cart-page/', product_cart_page, name='product-cart-page'),
    path('product-checkout-page/', product_checkout_page, name='product-checkout-page'),
    path('product-wishlist-page/', product_wishlist_page, name='product-wishlist-page'),
    path('product-frequently-questions-page/', product_frequently_questions, name='product-frequently-questions-page'),
    path('product-blog_main-page/', product_blog, name='product-blog-page'),
    path('product-blog_main-page/<int:blog_id>/', product_blog_details_page, name='product-blog-details-page'),
    path('my-account-page/', my_account, name='my-account'),
    path('login-page/', login_view, name='login'),
    path('register-page/', register_page, name='register'),
    path('about-page/', about_page, name='about'),
    path('contact-page/', contact_page, name='contact'),
]
from django.shortcuts import render


def product_cart_page(request):
    return render(request=request,
                  template_name='app/shop_main/cart_page.html')





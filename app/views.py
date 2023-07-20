from django.shortcuts import render


def index(request):
    return render(request=request,
                  template_name='app/index.html')


def shop_view(request):
    return render(request=request,
                  template_name='app/shop.html')


def product_detail_view(request):
    return render(request=request,
                  template_name='app/product-details.html')

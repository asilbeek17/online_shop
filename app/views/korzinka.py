from django.shortcuts import render

from app.models import Cart


def header(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.cartitem_set.all()
        cart_total = sum(item.total for item in cart_items)
    else:
        cart_items = []
        cart_total = 0
    return render(request=request,
                  template_name='app/main/header.html',
                  # context={'cart': cart})
                  context={"cart_items": cart_items, "cart_total": cart_total})


def sticky(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.cartitem_set.all()
        cart_total = sum(item.total for item in cart_items)
    else:
        cart_items = []
        cart_total = 0
    return render(request=request,
                  template_name='app/main/sticky.html',
                  # context={'cart': cart})
                  context={"cart_items": cart_items, "cart_total": cart_total})
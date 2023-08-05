from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from app.models import Product, Wishlist, Cart


@login_required(login_url='login')
def product_wishlist_page(request):
    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        cart_items = cart.cartitem_set.all()
        cart_total = sum(item.total for item in cart_items)
    else:
        cart_items = []
        cart_total = 0
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.product.all()
    return render(request=request,
                  template_name='app/shop_main/wishlist_page.html',
                  context={"products": products,
                           "cart_items": cart_items, "cart_total": cart_total})


def add_wishlist_view(request, product_id):
    product = get_object_or_404(klass=Product, id=product_id)

    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.product.add(product)
    return redirect("product-wishlist-page")


def delete_wishlist_view(request, product_id):
    product = get_object_or_404(klass=Product, id=product_id)

    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.product.remove(product)
    return redirect('product-wishlist-page')

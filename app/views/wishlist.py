from django.shortcuts import render, redirect, get_object_or_404

from app.models import Product, Wishlist


def product_wishlist_page(request):
    if request.user.is_authenticated:
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        products = wishlist.product.all()
        return render(request=request,
                      template_name='app/shop_main/wishlist_page.html',
                      context={"products":products})
    else:
        return redirect('login')


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


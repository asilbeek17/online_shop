from django.shortcuts import render, redirect

from app.form import ProductModelForm
from app.models import Product, Category, Blog


def index_view(request):
    laptops = Product.objects.filter(category__title='Laptop')
    products = Product.objects.order_by('-price').all()
    blogs = Blog.objects.all()[:3]
    return render(request=request,
                  template_name='app/main/index.html',
                  context={"products":products,
                           "laptops":laptops,
                           'blogs':blogs})


def shop_view(request):
    products = Product.objects.all()[:4]
    products_right = Product.objects.order_by('-price').all()[:3]
    return render(request=request,
                  template_name='app/shop_main/shop.html',
                  context={"products":products,
                           "products_right":products_right})


def product_details_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request=request,
                  template_name='app/shop_main/product_details.html',
                  context={'product':product})


def add_product_view(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_main')
    form = ProductModelForm()
    return render(request=request,
                  template_name='app/add_product.html',
                  context={"form":form,
                           "categories":categories})


def product_error404(request):
    return render(request=request,
                  template_name='app/shop_main/error404.html')


def product_compare_page(request):
    return render(request=request,
                  template_name='app/shop_main/compare_page.html')


def product_cart_page(request):
    return render(request=request,
                  template_name='app/shop_main/cart_page.html')


def product_checkout_page(request):
    return render(request=request,
                  template_name='app/shop_main/checkout_page.html')


def product_wishlist_page(request):
    return render(request=request,
                  template_name='app/shop_main/wishlist_page.html')


def product_frequently_questions(request):
    return render(request=request,
                  template_name='app/pages_main/frequently-questions.html')


def product_blog(request):
    return render(request=request,
                  template_name='app/blog_main/blog.html')


def product_blog_details_page(request):
    return render(request=request,
                  template_name='app/blog_main/blog-details.html')


def my_account(request):
    return render(request=request,
                  template_name='app/pages_main/my_account.html')


def login_view(request):
    return render(request=request,
                  template_name='app/pages_main/login.html')


def register_page(request):
    return render(request=request,
                  template_name='app/pages_main/register.html')


def about_page(request):
    return render(request=request,
                  template_name='app/about.html')


def contact_page(request):
    return render(request=request,
                  template_name='app/contact.html')




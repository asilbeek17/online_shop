from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from app.form import ProductModelForm, FeedbackModelForm, PostModelForm
from app.models import Product, Category, Blog, User, Post


def index_view(request):
    laptops = Product.objects.filter(category__title='Laptop')
    products = Product.objects.order_by('-price').all()
    blogs = Blog.objects.all()[:3]
    return render(request=request,
                  template_name='app/main/index.html',
                  context={"products": products,
                           "laptops": laptops,
                           'blogs': blogs})

                            
def shop_view(request):
    products = Product.objects.all()
    paginator = Paginator(object_list=products,
                          per_page=5)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(number=page_number)
    query = request.GET.get('query')
    if request.GET.get("sort_by") == 'title':
        product_list = Product.objects.order_by('title')[:5]

    if request.GET.get("sort_by") == 'price':
        product_list = Product.objects.order_by('-price')[:5]
        
    if query:
        product_list = Product.objects.filter(Q(title__icontains=query) |
                                              Q(category__title__icontains=query))
        
    return render(request=request,
                  template_name='app/shop_main/shop.html',
                  context={"product_list": product_list,
                           "query":query})


def product_blog_details_page(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    products = Product.objects.all()[:3]
    posts = Post.objects.all()
    paginator = Paginator(object_list=posts,
                          per_page=5)
    page_number = request.GET.get('page')
    post_list = paginator.get_page(number=page_number)
    if request.method == "POST":
        form = PostModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PostModelForm()

    return render(request=request,
                  template_name='app/blog_main/blog-details.html',
                  context={'blog': blog,
                           "form":form,
                           "post_list":post_list,
                           "products":products})



def product_blog(request):
    blog = Blog.objects.all()
    paginator = Paginator(object_list=blog,
                          per_page=4)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(number=page_number)
    query = request.GET.get('query', '')
    if request.GET.get('sort_by') == 'title':
        blog_list = Product.objects.order_by('title')[:4]

    if query:
        blog_list = Blog.objects.filter(title__icontains=query)

    return render(request=request,
                  template_name='app/blog_main/blog.html',
                  context={'blog': blog,
                           "blog_list":blog_list})


def product_details_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    return render(request=request,
                  template_name='app/shop_main/product_details.html',
                  context={'product':product})


def add_product_view(request):
    categories = Category.objects.all()
    users = User.objects.all()
    if request.method == "POST":
        form = ProductModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('shop_main')
    form = ProductModelForm()
    return render(request=request,
                  template_name='app/add_product.html',
                  context={"form": form,
                           "categories": categories,
                           "users":users})


def edit_product(request, product_id):
    categories = Category.objects.all()
    users = User.objects.all()
    product = Product.objects.filter(id=product_id).first()
    if request.method == "POST":
        form = ProductModelForm(data=request.POST,
                                files=request.FILES,
                                instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            
            return redirect('product-details', product.id)

    form = ProductModelForm(instance=product)
    return render(request=request,
                  template_name='app/edit_product.html',
                  context={"form":form,
                           'users':users,
                           "categories":categories})


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()

    if product:
        product.delete()
        return redirect('shop_main')


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





def about_page(request):
    return render(request=request,
                  template_name='app/about.html')


def contact_page(request):
    if request.method == "POST":
        form = FeedbackModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProductModelForm()
    return render(request=request,
                  template_name='app/contact.html',
                  context={"form": form})

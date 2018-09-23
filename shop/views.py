from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForms


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_porduct_form = CartAddProductForms()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_porduct_form})

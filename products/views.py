from django.shortcuts import render
from .models import Category, Brand, Warranty, Seller, Product

def product_list(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    warranties = Warranty.objects.all()
    sellers = Seller.objects.all()
    products = Product.objects.all()

    # Apply filters if provided in the request
    selected_category = request.GET.get('category')
    selected_brand = request.GET.get('brand')
    selected_warranty = request.GET.get('warranty')
    selected_seller = request.GET.get('seller')

    if selected_category:
        products = products.filter(category__id=selected_category)
    if selected_brand:
        products = products.filter(brand__id=selected_brand)
    if selected_warranty:
        products = products.filter(warranty__id=selected_warranty)
    if selected_seller:
        products = products.filter(seller__id=selected_seller)

    context = {
        'categories': categories,
        'brands': brands,
        'warranties': warranties,
        'sellers': sellers,
        'products': products
    }

    # context = {"hello":"hi"}

    return render(request, 'product_list.html', context)

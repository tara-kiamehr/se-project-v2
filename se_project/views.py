from django.shortcuts import render
from product.models import product

def home(request):
    products = product.objects.all()  # دریافت همه محصولات
    return render(request, 'index.html', {'products': products})  # تغییر به 'products'
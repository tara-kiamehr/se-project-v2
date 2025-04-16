from django.shortcuts import render
from product.models import product
from contactus_app.models import footer

def home(request):

 #   if request.method == "POST":
 #       fname = request.POST.get('fname')
 #       email = request.POST.get('email')
 #       sub = request.POST.get('sub')
  #      body = request.POST.get('body')
   #     footer.objects.create(fname=fname, email=email, sub=sub, body=body)

    products = product.objects.all()  # دریافت همه محصولات
    footers = footer.objects.get(id=1)
    
    return render(request, 'index.html', {'products': products, 'footer':footers})  
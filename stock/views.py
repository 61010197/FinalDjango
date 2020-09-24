from django.shortcuts import render
from .models import Product

def index(request):
    # html = "<html><body>Welcome to KKK</body></html>"
    # return HttpResponse(html)
    products = Product.objects.all()
    return render(request, 'frontend/index.html',{'products': products})
def review(request):
    return render(request, 'frontend/review.html')
def contact(request):
    return render(request, 'frontend/contact.html')

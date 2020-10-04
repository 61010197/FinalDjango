from django.shortcuts import render
from .models import Product

def index(request):
    # html = "<html><body>Welcome to KKK</body></html>"
    # return HttpResponse(html)
    return render(request, 'frontend/index.html')
def about(request):
    return render(request, 'frontend/about.html')
def contact(request):
    return render(request, 'frontend/contact.html')

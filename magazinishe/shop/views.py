from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def cart_view(request):
    return render(request, 'cart.html')

def categories_view(request):
    return render(request, 'categories.html')

def products_view(request):
    return render(request, 'products.html')

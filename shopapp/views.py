from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ContactForm

# Create your views here.

def home_page(request):
    items = Product.objects.all()
    categories = Category.objects.all()

    if request.method == "POST" and request.POST.get('category_id'):
        items = Product.objects.filter(category=request.POST.get('category_id'))
    else:
        items = Product.objects.all()

    context1 = {
        'categories': Category.objects.all(),
        'items': items
    }

    return render(request, 'shopapp/index.html', context1)




def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context = {'form':form}
    return render(request, 'shopapp/index.html', context)


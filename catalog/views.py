from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.

def home_page(request):
    context = {
        'product_list': Product.objects.all(),
        'title': 'Skystore',
        'subtitle': 'Skystore - это отличный вариант хранения ваших плагинов и примеров кода, который вы бы хотели продать'
    }
    return render(request, 'catalog/home.html', context)


def contacts_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name:{name}, phone:{phone}, message:{message}")
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    products = Product.objects.get(id=pk)
    context = {
        'product': products,
        'title': f'{products.name}'
    }
    return render(request, 'catalog/product.html', context)

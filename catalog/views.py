from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Category


# def home_page(request):
#     context = {
#         'product_list': Product.objects.all(),
#         'title': 'Skystore'
#     }
#     return render(request, 'catalog/home.html', context)


class HomepageListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Skystore'
    }


# def contacts_page(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"name:{name}, phone:{phone}, message:{message}")
#     context = {
#         'title': 'Контакты'
#     }
#     return render(request, 'catalog/contacts.html', context)


class ContactsPageView(View):
    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"name:{name}, phone:{phone}, message:{message}")
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)


# def product(request, pk):
#     products = Product.objects.get(id=pk)
#     context = {
#         'product': products,
#         'title': f'{products.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)
#

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'title': f'{product.name}'
        }
        return render(request, 'catalog/product_detail.html', context)

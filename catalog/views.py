from django.forms import formset_factory, inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Create Product'
    }

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.name)
        new_mat.save()
        self.object = form.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    extra_context = {
        'title': 'Update Product'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object,)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.name)
        new_mat.save()
        self.object = form.save()
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view', args=[self.object.pk])


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Skystore'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        # for product in queryset:
        #     version = product.version_set.all().filter(is_current=True).first()
        #     product.version = version
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        for object in context['product_list']:
            active_version = Version.objects.filter(product=object, is_current=True).last()
            if active_version:
                object.active_version_number = active_version.version_number
            else:
                object.active_version_number = None
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['title'] = product.name
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'title': 'Delete Post'
    }

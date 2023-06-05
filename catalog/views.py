from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import MyForm, ProductForm, ProductVersion
from .models import Product, Blog, Version


# Create your views here.
# def index(request):
#     context = {'object_list': Product.objects.all()}
#     return render(request, 'catalog/product_list.html', context)


class ProductView(ListView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = 'название'

        return context_data


class ProductDetail(DetailView):
    model = Product


#
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form_formset.html'

    def get_success_url(self):
        obj = self.object
        return reverse('catalog:details', args=[obj.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=ProductVersion, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        form_valid = super().form_valid(form)
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return form_valid


class BlogView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(publication_sign=True)
        return queryset


class BlogDetail(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_amount += 1
        obj.save()
        return obj


class BlogCreate(CreateView):
    model = Blog
    form_class = MyForm

    def get_success_url(self):
        obj = self.object
        return reverse('catalog:blog_detail', args=[obj.pk])


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_view')


class BlogUpdate(UpdateView):
    model = Blog
    fields = ('header', 'content', 'content', 'creation_date')

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Product, Blog


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


# def details(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {'object': product_item
#                }
#     return render(request, 'catalog/product_detail.html', context)


# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#         price_for_buy = request.POST.get('price_for_buy')
#         creation_date = request.POST.get('creation_date')
#         Product.objects.create(name=name, description=description, category=category, price_for_buy=price_for_buy,
#                                creation_date=creation_date)
#
#     return render(request, 'catalog/product_form.html')
class ProductCreate(CreateView):
    model = Product
    fields = ('name', 'description', 'creation_date', 'price_for_buy')
    success_url = reverse_lazy('catalog:index')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


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
    fields = ('header', 'content', 'content', 'creation_date')
    success_url = reverse_lazy('catalog:blog_view')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_view')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ('header', 'content', 'content', 'creation_date')







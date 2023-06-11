from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
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


class ProductView(LoginRequiredMixin, ListView):
    model = Product




class ProductDetail(DetailView):
    model = Product


#
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):

        instance = form.save()
        instance.author = self.request.user

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')


class ProductUpdate( UserPassesTestMixin, UpdateView):
    model = Product
  #  permission_required = 'catalog.change_product'
    form_class = ProductForm
    template_name = 'catalog/product_form_formset.html'

    def test_func(self):
        user = self.request.user
        obj = self.get_object()

        return user.groups.filter(name='moderators').exists() or user == obj.author

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     obj = self.get_object()
    #     if obj.author == self.request.user:
    #         return form
    #
    #     if not self.request.user.has_perm('catalog.can_ban_publication_product'):
    #         form.fields['publication_sign'].disabled = True  # Запрещаем изменение поля "категория"
    #     if not self.request.user.has_perm('catalog.can_change_description_product'):
    #         form.fields['description'].disabled = True  # Запрещаем изменение поля "категория"
    #     if not self.request.user.has_perm('catalog.can_change_category_product'):
    #         form.fields['category'].disabled = True  # Запрещаем изменение поля "категория"
    #     return form



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


class BlogUpdate( UpdateView):
    model = Blog
    fields = ('header', 'content', 'content', 'creation_date')



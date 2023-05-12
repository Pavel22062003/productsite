from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    context = {'object_list': Product.objects.all()}
    return render(request, 'catalog/index.html', context)


def details(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {'object': product_item
               }
    return render(request, 'catalog/details.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        description = request.POST.get('description')
        category = request.POST.get('category')
        price_for_buy = request.POST.get('price_for_buy')
        creation_date = request.POST.get('creation_date')
        Product.objects.create(name=name, description=description, category=category,price_for_buy=price_for_buy,creation_date=creation_date)

    return render(request, 'catalog/add.html')
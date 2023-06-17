from catalog.models import Category


def all_category():

    categories = Category.objects.all()
    return categories
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductView, ProductDetail, ProductCreate, ProductDeleteView, BlogView, BlogDetail, \
    BlogCreate, BlogDelete, BlogUpdate

app_name = CatalogConfig.name

urlpatterns = [

    path('', ProductView.as_view(), name='index'),
    path('details/<int:pk>/', ProductDetail.as_view(), name='details'),
    path('add/', ProductCreate.as_view(), name='add'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('blog/', BlogView.as_view(), name='blog_view'),
    path('blog/detail/<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('blog/create', BlogCreate.as_view(), name='blog_create'),
    path('blog/delete/<int:pk>', BlogDelete.as_view(), name='blog_delete'),
    path('blog/update/<int:pk>/', BlogUpdate.as_view(), name='blog_update')


]

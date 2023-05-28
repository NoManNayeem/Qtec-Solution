from django.urls import include, path,re_path
from django.contrib import admin
from .views import product_list



admin.site.site_header = 'Qtec'
admin.site.index_title = 'Qtec Title'
admin.site.site_title = 'Category'


urlpatterns = [
    path('products/', product_list, name='product_list'),
    ]
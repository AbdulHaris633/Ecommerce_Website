from django.urls import path
from .views import category_list, get_product_by_category_id,homepage

APP_NAME = "catalogue"
 
urlpatterns = [
    path("categories/list/", category_list, name="category_list"),
    path("products/list/", get_product_by_category_id, name="product_list"),
    path("products/list/<uuid:category_id>/", get_product_by_category_id,name="product_list_by_category") ,
    path("homepage/",homepage, name="homepage1"),   
]
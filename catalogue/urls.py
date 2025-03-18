from django.urls import path

from .views import category_list, get_product_by_category_id, homepage, product_detail, product_stats,homepage2

APP_NAME = "catalogue"    

urlpatterns = [
    path("categories/list/", category_list, name="category_list"),  
    path(
        "categories/list/<uuid:category_id>",
        get_product_by_category_id,
        name="product_list",
    ),
    path("products/list/", get_product_by_category_id, name="product_list"),
    path(
        "products/list/<uuid:category_id>/",
        get_product_by_category_id,
        name="product_list_by_category", 
    ),
    path("homepage/", homepage, name="homepage1"),
    path("adminhomepage/", homepage2, name="homepage2"),  
    path("product/detail/<uuid:product_id>/", product_detail, name="product_detail"),
    path('product/<uuid:product_id>/stats/', product_stats, name='product_stats'), 
 
    
]  
    
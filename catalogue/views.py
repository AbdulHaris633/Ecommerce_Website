from django.shortcuts import render
from .models import Category, Product  




def category_list(request): 
    all_cat = Category.objects.all() 
    context = {
        "categories": all_cat 
    }
    return render(request, "catalogue/category_list.html", context) 
  

def get_product_by_category_id(request, category_id=None):
    all_product = Product.objects.all()
    all_category = Category.objects.all() 
    
    if category_id:
        products = all_product.filter(category_id=category_id)
    else:
        products = all_product 

    context = {
        "all_product": products,
        "all_category": all_category,   
        "selected_category": category_id
    }

    return render(request, "catalogue/product_list.html", context)


def homepage(request):
    
    return render(request,"catalogue/homepage.html") 



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)  
    context = {
        'product': product  
    }
    return render(request, 'catalogue/product_detail.html', context)


  

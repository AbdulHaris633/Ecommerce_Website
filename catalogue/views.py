from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.db.models import F
from .models import Category, Product
from django.http import JsonResponse

@login_required 
def category_list(request):
    # print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}") 
    all_cat = Category.objects.all()
    context = {"categories": all_cat}
    return render(request, "catalogue/category_list.html", context)

@login_required 
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
        "selected_category": category_id,
    }

    return render(request, "catalogue/product_list.html", context)

@login_required 
def homepage(request):

    return render(request, "catalogue/homepage.html")

@login_required     
def homepage2(request):

    return render(request, "catalogue/adminhomepage.html")


@login_required 
def product_detail(request, product_id): 
    product = Product.objects.get(id=product_id)
    Product.objects.filter(id=product_id).update(views_in_24_hours=F('views_in_24_hours') + 1)
    # Refresh the product instance to get the updated value
    product.refresh_from_db()
    context = {"product": product}
    return render(request, "catalogue/product_detail.html", context)



def product_stats(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = {
            "label": product.name, 
            "sold_in_24_hours": product.sold_in_24_hours or 0, 
            "views_in_24_hours": product.views_in_24_hours or 0,  
            "total_sold": product.total_sold or 0  
        }
        return JsonResponse(data) 
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404) 


  
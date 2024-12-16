from django.shortcuts import render
from django.http import JsonResponse
from catalogue.models import Product
from .basket import Basket
from uuid import UUID
from django.shortcuts import redirect 

def add_to_basket(request, product_id: UUID): 
    basket = Basket(request)
    product = Product.objects.get(id=product_id) 
    quantity = int(request.POST.get('quantity', 1))
    basket.add(product=product, quantity=quantity) 
    return redirect('basket_detail')

def remove_from_basket(request, product_id: UUID):
    print(f"Product to remove: {product_id}")
    basket = Basket(request)
    print("=========================================") 
    basket.remove(product_id)
    return redirect('basket_detail')  

def basket_detail(request): 
    basket = Basket(request)  
    return render(request, 'basket/basket.html', {'basket': basket}) 

def basket(request):
    return {'basket': Basket(request)}  

def delete_from_basket(request, product_id: UUID):
    print(f"Product to remove: {product_id}")
    basket = Basket(request)
    print("=========================================") 
    basket.delete(product_id)
    return redirect('basket_detail')   

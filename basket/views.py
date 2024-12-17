from uuid import UUID

from django.shortcuts import redirect, render

from catalogue.models import Product

from .basket import Basket


def add_to_basket(request, product_id: UUID):
    basket = Basket(request) # Step 1
    p = Product.objects.get(id=product_id)
    quantity = int(request.POST.get("quantity", 1))
    basket.add(p, quantity=quantity) # step 2
    return redirect("basket_detail")


def remove_from_basket(request, product_id: UUID):
    print(f"Product to remove: {product_id}")
    basket = Basket(request)
    basket.remove(product_id)
    return redirect("basket_detail")


def basket_detail(request):
    basket = Basket(request)
    # print(dir(basket)) 
    return render(request, "basket/basket.html", {"basket": basket})


def basket(request): 
    return {"basket": Basket(request)}


def delete_from_basket(request, product_id: UUID):
    basket = Basket(request)
    basket.delete(product_id)
    return redirect("basket_detail")  

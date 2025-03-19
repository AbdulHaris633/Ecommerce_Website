from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from uuid import UUID 
from .basket import Basket 
from django.shortcuts import redirect, render
from catalogue.models import Product
from .basket import Basket 

@login_required
def add_to_basket(request, product_id: UUID):  
    if request.method == "POST":
        basket = Basket(request)  
        product = get_object_or_404(Product, id=product_id)
        requested_quantity = int(request.POST.get("quantity", 1))  

        # Check if the requested quantity exceeds the available stock
        if requested_quantity > product.quantity:
            return JsonResponse({"error": f"Only {product.quantity} items available.", "success": False}, status=400)

        # Add product to the basket
        basket.add(product, quantity=requested_quantity)

        # Reduce the product's quantity in the database
        product.quantity -= requested_quantity
        product.save()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":  # Check if AJAX request
            return JsonResponse({"message": f"{product.name} has been added to your basket.", "success": True})

        return redirect("basket_detail")  # For normal form submission

    return JsonResponse({"error": "Invalid request"}, status=400) 
  
@login_required
def remove_from_basket(request, product_id: UUID):
    print(f"Product to remove: {product_id}")  

    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)

    # Get the quantity before removal
    removed_quantity = basket.get_quantity(product_id)

    # Restore stock in database
    if removed_quantity > 0:
        product.quantity += 1  # Add back only one unit (since we're decreasing by 1)
        product.save()

    
    basket.remove(product_id)

    return redirect("basket_detail") 

@login_required
def basket_detail(request):
    basket = Basket(request)
    # print(dir(basket))
    return render(request, "basket/basket.html", {"basket": basket})

@login_required
def basket(request):
    return {"basket": Basket(request)}

@login_required
def delete_from_basket(request, product_id: UUID):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)

    # Get the current quantity in the basket
    quantity_to_restore = basket.get_quantity(product_id)

    # Restore all quantity back to the database
    if quantity_to_restore > 0:
        product.quantity += quantity_to_restore
        product.save()


    basket.delete(product_id)

    return redirect("basket_detail")    

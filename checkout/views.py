from catalogue.models import Product
from django.conf import settings
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, redirect, get_object_or_404  
from django.contrib import messages

# @csrf_exempt     
@login_required  
def checkout(request):
    basket = request.session.get(settings.BASKET_SESSION_ID, {})
    items = []

    for product_id, item in basket.items():
        product_name = item.get("product_name", "Unknown Product")
        quantity = int(item["quantity"])
        price = float(item["price"])
        item_total = quantity * price
        items.append(
            {
                "product_id": product_id,  # Store product ID for updating the database
                "product": product_name,
                "quantity": quantity,
                "price": price,
                "total": item_total,
            }
        )

    total_price = sum(item["total"] for item in items)

    if request.method == "POST":
        shipping_address = request.POST.get("shipping_address")

        if not shipping_address:  # Ensure address is entered
            messages.error(request, "Shipping address is required!")
            return render(request, "checkout/checkout.html", {"items": items, "total_price": total_price})

        # **Update product sales data**
        for item in items:
            product = Product.objects.filter(id=item["product_id"]).first()
            if product:
                product.total_sold += item["quantity"]
                product.sold_in_24_hours += item["quantity"]
                product.save()

        # Store order details in session before redirecting
        request.session["order_details"] = {
            "items": items,
            "total_price": total_price,
            "shipping_address": shipping_address,
        } 

        # Clear the basket after checkout
        request.session[settings.BASKET_SESSION_ID] = {}  
        request.session.modified = True   

        return redirect("invoice")  # Redirect to invoice page

    # **Render checkout page on GET request**
    return render(request, "checkout/checkout.html", {"items": items, "total_price": total_price})
from django.shortcuts import render
from django.conf import*
from django.http import HttpResponse

# MC146416


def checkout(request):
    # Retrieve basket data from session
    basket = request.session.get(settings.BASKET_SESSION_ID, {})
    items = []

    for product_id, item in basket.items():
        product_name = item.get('product_name', 'Unknown Product')
        item_total = int(item['quantity']) * float(item['price'])  # Calculate total for each item
        items.append({
            'product': product_name,  
            'quantity': item['quantity'],  
            'price': item['price'],
            'total': item_total, 
        })
    
    # Calculate total price for the basket
    total_price = sum(item['total'] for item in items)

    return render(request, 'checkout/checkout.html', {
        'items': items,
        'total_price': total_price, 
    })
 
 
def success(request): 
    return HttpResponse("payment completed")  
     
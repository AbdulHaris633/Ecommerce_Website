from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta
import hashlib
import hmac
from django.conf import settings

# MC146416

# Configuration
JAZZCASH_MERCHANT_ID = "MC146416"
JAZZCASH_PASSWORD = "1351442wu4"
JAZZCASH_RETURN_URL = "http://13.48.45.103/payment/success/"
JAZZCASH_INTEGRITY_SALT = "3x2s596214"


@csrf_exempt
def checkout(request):
    basket = request.session.get(settings.BASKET_SESSION_ID, {}) 
    items = []

    for product_id, item in basket.items():
        product_name = item.get('product_name', 'Unknown Product')
        quantity = int(item['quantity'])
        price = float(item['price'])
        item_total = quantity * price
        items.append({
            'product': product_name,
            'quantity': quantity,
            'price': price,
            'total': item_total,
        })

    total_price = sum(item['total'] for item in items)

    current_datetime = datetime.now()
    pp_TxnDateTime = current_datetime.strftime('%Y%m%d%H%M%S')
    pp_TxnExpiryDateTime = (current_datetime + timedelta(hours=1)).strftime('%Y%m%d%H%M%S')
    pp_TxnRefNo = 'T' + pp_TxnDateTime

    post_data = {
        "pp_Version": "1.0",
        "pp_TxnType": "MWALLET",
        "pp_Language": "EN",
        "pp_MerchantID": JAZZCASH_MERCHANT_ID, 
        "pp_SubMerchantID": "",
        "pp_Password": JAZZCASH_PASSWORD, 
        "pp_BankID": "TBANK",
        "pp_ProductID": "RETL",
        "pp_TxnRefNo": pp_TxnRefNo,
        "pp_Amount": int(total_price * 100),  # Convert to paisa
        "pp_TxnCurrency": "PKR",
        "pp_TxnDateTime": pp_TxnDateTime,
        "pp_BillReference": "billRef",
        "pp_Description": "Basket purchase",
        "pp_TxnExpiryDateTime": pp_TxnExpiryDateTime,
        "pp_ReturnURL": JAZZCASH_RETURN_URL,
        "pp_SecureHash": "",
        "ppmpf_1": "1",
        "ppmpf_2": "2",
        "ppmpf_3": "3",
        "ppmpf_4": "4",
        "ppmpf_5": "5",
    }

    sorted_string = '&'.join(f"{key}={value}" for key, value in sorted(post_data.items()) if value)
    pp_SecureHash = hmac.new(
        JAZZCASH_INTEGRITY_SALT.encode(),
        sorted_string.encode(),
        hashlib.sha256
    ).hexdigest()
    post_data['pp_SecureHash'] = pp_SecureHash

    return render(request, 'checkout/checkout.html', {
        'items': items,
        'total_price': total_price,
        'post_data': post_data,
    })


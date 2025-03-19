from django.conf import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@csrf_exempt

@login_required
def invoice(request):
    order_details = request.session.get("order_details", {})

    if not order_details or not order_details.get("items"):
        return redirect("checkout")

    return render(request, "payment/invoice.html", order_details)        
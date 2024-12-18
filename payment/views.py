from django.views.decorators.csrf import csrf_exempt
from django.conf import*
from django.http import HttpResponse
 
@csrf_exempt
def success(request): 
    return HttpResponse("payment completed")  

def fail(request): 
    return HttpResponse("payment failed")      
     
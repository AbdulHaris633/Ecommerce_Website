
from django.conf import*
from django.http import HttpResponse
 
def success(request): 
    return HttpResponse("payment completed")  

def fail(request): 
    return HttpResponse("payment failed")    
     
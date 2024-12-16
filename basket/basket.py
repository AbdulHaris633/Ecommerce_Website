from decimal import Decimal
from urllib import request
from django.conf import settings
from catalogue.models import Product 



class Basket:
    
    def __init__(self,request): 
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID]={}
        self.basket = basket 
        print(f"Initialized basket: {self.basket}")   
        
    def add(self,product, quantity=1, override_quantity=False):
        
        product_id = str(product.id) 
         
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0, 'price': str(product.price)}

        if override_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity

        self.save()
        
    def __iter__(self):
       
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    
    def delete(self, product_id): 
        print(f"Removing product ID: {product_id}")  
        product_id = str(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
            print(f"Product ID {product_id} removed from basket.")
            self.save()
        else:
            print(f"Product ID {product_id} not found in basket.") 
    
    


                    
    def get_total_price(self):
        """Calculate the total price of the items in the basket"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())
    
    
    def remove(self, product_id):

     product_id = str(product_id)  # Ensure the product ID is a string

     if product_id in self.basket:
        if self.basket[product_id]['quantity'] > 1:
            # Decrease quantity by 1
            self.basket[product_id]['quantity'] -= 1
            print(f"Decreased quantity for product ID {product_id}. New quantity: {self.basket[product_id]['quantity']}")
        else:
            # If quantity is 1, remove the product from the basket
            del self.basket[product_id]
            print(f"Product ID {product_id} removed from basket.")
        
        # Save changes
        self.save()
     else:
        print(f"Product ID {product_id} not found in basket.") 


         
    def clear(self):
        """Clear the basket"""
        del self.session[settings.BASKET_SESSION_ID]
        self.save() 
    
    def save(self):
        self.session.modified = True 
        print("Basket saved. Session marked as modified.")   
    

    
    def update(self):
        pass 
    
    def show(self):
        pass
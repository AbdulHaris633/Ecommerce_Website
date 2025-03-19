from decimal import Decimal

from django.conf import settings

from catalogue.models import Product


class Basket:
  
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket 
        
    def get_quantity(self, product_id):
        """Retrieve the quantity of a product in the basket."""
        product_id = str(product_id) 
        return self.basket.get(product_id, {}).get("quantity", 0)

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
 
        if product_id not in self.basket:
            self.basket[product_id] = {
                "quantity": 0,
                "price": str(product.price),
                "product_name": product.name,
            }

        if override_quantity:
            self.basket[product_id]["quantity"] = quantity
        else:
            self.basket[product_id]["quantity"] += quantity

        self.save()  
    

    def __iter__(self):

        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item
    

    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
            print(f"Product ID {product_id} removed from basket.")
            self.save()
        else:
            print(f"Product ID {product_id} not found in basket.")

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.basket.values()
        )

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.basket:
            if self.basket[product_id]["quantity"] > 1:
                self.basket[product_id]["quantity"] -= 1
            else:
                del self.basket[product_id]
            self.save()
        else:
            print(f"Product ID {product_id} not found in basket.")

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True

    def __str__(self):
        return "This is my baset"

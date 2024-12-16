from django.db import models
import uuid
from django.core.validators import MinValueValidator

class ProductClass(models.Model):
    id= models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    id= models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=50,null=True)
    description=models.TextField(max_length=255,blank=True)
    image=models.ImageField(upload_to="images/",blank=True)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
     
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    id= models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=50,null=True)   
    rating=models.DecimalField(max_digits=3,decimal_places=2,default=0.00,null=True,validators=[MinValueValidator(0)])
    price=models.FloatField(null=True,blank=True,default=0.0) 
    description=models.TextField(max_length=255,blank=True,null=True)
    image=models.ImageField(upload_to="images/",blank=True,null=True)
    
    def __str__(self):
        return self.name   
    
    

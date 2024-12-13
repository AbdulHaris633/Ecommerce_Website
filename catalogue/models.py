from django.db import models
import uuid

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
    description=models.TextField(max_length=255,blank=True)
    image=models.ImageField(upload_to="images/",blank=True)
    
    def __str__(self):
        return self.name  
    
    

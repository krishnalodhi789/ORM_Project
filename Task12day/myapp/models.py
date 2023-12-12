from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    
    def __str__(self) ->str:
        return self.user.username
    
    
class Product(models.Model):
    category = models.CharField(max_length=50) 
    price = models.CharField(max_length=50) 
    product_image = models.ImageField(upload_to='')
    title = models.CharField(max_length=50) 
    description = models.TextField(max_length=300)
    sale = models.BooleanField(default=False)
    buyer_id= models.IntegerField(null=True, blank=True)
    
    def __int__(self) -> int:
        return self.price
    
class Buyer_wallet(models.Model):
    buyer = models.ForeignKey(Buyer, verbose_name="_buyer", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="_product", on_delete=models.CASCADE)
    
    def __int__(self) -> int:
        return self.buyer.id
    

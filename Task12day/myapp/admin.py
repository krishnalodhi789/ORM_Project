from django.contrib import admin
from .models import Buyer, Product, Buyer_wallet
# Register your models here.
admin.site.register(Buyer)
admin.site.register(Product)

@admin.register(Buyer_wallet)
class Buyer_wallet_model(admin.ModelAdmin):
    list_display=['buyer_id','product_id']
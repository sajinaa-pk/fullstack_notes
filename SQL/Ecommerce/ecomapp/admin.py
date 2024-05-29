from django.contrib import admin
from . models import Pproduct
# Register your models here.
@admin.register(Pproduct)
class PproductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

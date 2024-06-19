from django.contrib import admin
from .models import Link
from .models import Customer
from .models import Wish
# Register your models here.

admin.site.register(Link)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','city','mobile']

admin.site.register(Wish)



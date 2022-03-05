from django.contrib import admin
from .models import ShopData
from .models import Comments


class ShopDataAdmin(admin.ModelAdmin):
    search_fields = ['Name']

# Register your models here.


admin.site.register(ShopData, ShopDataAdmin)
admin.site.register(Comments)
from django.contrib import admin
from .models import Seller,Product,Client,Admin,Order

# Register your models here.


class AdminAdmin(admin.ModelAdmin):
    #prepopulated_fields={'name':('name',)}
    list_display=[

        
        'name',
        'email',
        'phone',
        'nb_weekly_prod_vendus',
        'nb_clients',
        'nb_vendeurs',

    ]




admin.site.register(Admin,AdminAdmin)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Order)


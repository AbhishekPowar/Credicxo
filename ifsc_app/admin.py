from django.contrib import admin
from .models import Bank_Details

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bank_Details, BankAdmin)
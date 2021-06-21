from django.contrib import admin
from .models import LoanOffer,LoanRequest
# Register your models here.

admin.site.register(LoanRequest)
admin.site.register(LoanOffer)
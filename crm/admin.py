from django.contrib import admin
from .models import Order, StatusCrm, CommnetCrm
# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommnetCrm)

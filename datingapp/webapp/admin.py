from django.contrib import admin
from webapp.models import Booktickets

# Register your models here.
class AdminBookTicket(admin.ModelAdmin):
    list_display=['name','age','sex','email','address','tickets','date','adults','children','occassion','ordered',]

admin.site.register(Booktickets,AdminBookTicket)

from django.contrib import admin
from myApp.models import User,carInfo

class Carmanager(admin.ModelAdmin):
    list_display = ["id","brand","carName","carImg","saleVolume","price","manufacturer","rank","carModel",
                                "energyType","marketTime","insure","creteTime"]
    list_display_links = ["carName"]
    list_filter = ["energyType"]
    search_fields = ["carName"]
    date_hierarchy = "creteTime"
    list_per_page = 15
admin.site.register(carInfo,Carmanager)

class Usermanager(admin.ModelAdmin):
    list_display = ["id","username","password","creteTime"]
    date_hierarchy = "creteTime"

admin.site.register(User,Usermanager)


# Register your models here.

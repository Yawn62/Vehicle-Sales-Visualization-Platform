from myApp.models import *

def getAllCars():
    return carInfo.objects.all()
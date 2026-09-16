from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .utils import getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from .utils import getCenterRightData
from .utils import getCenteChangeData
from .utils import getBottomRightData
from myApp.models import User

@csrf_exempt
def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        message = ''
        print(uname,pwd)
        try:
            user = User.objects.get(username=uname,password=pwd)
            message = '登录成功'
            print(message)
            return JsonResponse({
                'username':uname,
                'message':message
            })
        except:
            return JsonResponse({
                'message':'登录失败'
            })

def center(request):
    if request.method == 'GET':
        sumCar,highVolume,topCar,mostModel,mostBrand,averagePrice = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        oilRate,electricRate,mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar':sumCar,
            'highVolume':highVolume,
            'topCar': topCar,
            'mostModel': mostModel,
            'mostBrand': mostBrand,
            'averagePrice': averagePrice,
            'lastSortList':lastSortList,
            'oilRate':oilRate,
            'electricRate':electricRate,
            'mixRate':mixRate
        })

def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList':lastPieList
        })

def bottomLeft(request):
    if request.method == 'GET':
        brandList,volumeList,priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandList':brandList,
            'volumeList':volumeList,
            'priceList':priceList
        })

def centerRight(request):
    if request.method == 'GET':
        realData = getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData':realData
        })

def centerRightChange(request,energyType):
    if request.method == 'GET':
        oilData,electricDataData = getCenteChangeData.getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricDataData
        return JsonResponse({
            'realData':realData
        })

def bottomRight(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse({
            'carData':carData
        })

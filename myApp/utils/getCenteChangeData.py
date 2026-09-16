import json
import time
from .getPublicData import *

def getCircleData():
    cars = list(getAllCars())
    oilData = []
    electricDataData = []
    for i in cars:
        if i.energyType == '汽油':
            oilData.append([i.carName,i.saleVolume,i.energyType])
        elif i.energyType == '纯电动':
            electricDataData.append([i.carName, i.saleVolume, i.energyType])
    oilData = oilData[:10]
    electricDataData = electricDataData[:10]
    return oilData,electricDataData
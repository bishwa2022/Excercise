# Exercise 9
#question 1
from tabulate import tabulate
class car:
    def __init__(self, regnumb, maxspd):
        self.regnum = regnumb
        self.maxspd = maxspd
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regnum,
            "Maximum speed": self.maxspd,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }
        return self.carStatus


carInfo = []
newCar = car("ABC-123", 142)
carInfo.append(newCar.info())
print(tabulate(carInfo, headers="keys"))

#question 2
class car:
    def __init__(self, regnum, maxspd):
        self.regnum = regnum
        self.maxspd = maxspd
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxspd:
            self.curSpeed = self.maxspd
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed


newCar = car("ABC-123", 142)
newCar.accelerate(30)
newCar.accelerate(70)
newCar.accelerate(50)
print("Current car's speed after accelerating:", newCar.curSpeed)
newCar.emergency()
print("Current car's speed after emergency:", newCar.curSpeed)

#question 3
class car:
    def __init__(self, regnum, maxspd):
        self.regnum = regnum
        self.maxspd = maxspd
        self.curSpeed = 0
        self.travelledDistance = 0

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxspd:
            self.curSpeed = self.maxspd
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance

newCar = car("ABC-123", 142)
newCar.accelerate(60)
print("Current car's speed:", newCar.curSpeed)
newCar.travelledDistance = 2000
print("Travelled distance:", newCar.travelledDistance, "km")
newCar.drive(1.5)
print("Travelled distance after 1.5 hours:", newCar.travelledDistance, "km")

#question 4
from tabulate import tabulate
import random
class car:
    def __init__(self, regnum, maxspd):
        self.regnum = regnum
        self.maxspd = maxspd
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regnum,
            "Maximum speed": self.maxspd,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxspd:
            self.curSpeed = self.maxspd
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance

carList = []
for i in range(1, 11):
    newCar = car("ABC-" + str(i), random.randint(100, 200))
    carList.append(newCar)

maxTravelledDistance = 0
while maxTravelledDistance < 10000:
    for i in range(10):
        carList[i].accelerate(random.randint(-10, 15))
        carList[i].drive(1)
        carList[i].info()
        if maxTravelledDistance < carList[i].travelledDistance:
            maxTravelledDistance = carList[i].travelledDistance

raceResult = []
for i in range(10):
    raceResult.append(carList[i].carStatus)
print(tabulate(raceResult, headers="keys"))"""







def py():
    pass
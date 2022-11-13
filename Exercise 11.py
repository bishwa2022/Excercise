# Exercise 11
#question 1
class Publication:
    def __init__(self, name):
       self.name = name

    def print_info(self):
        print(self.name, end= " ")

class Book(Publication):
    def __init__(self, name, author, page_num,):
        super().__init__(name)
        self.author = author
        self.page_num = page_num
    def print_info(self):
        super().print_info()
        print(" Author:" + self.author + "," + str(self.page_num) + "pages)")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("(chief editor" + ":" + self.editor + ")")


pubs = []
pubs.append(Magazine("Awesome Ghimire", "Subu Ghimire"))
pubs.append(Book("Compartment No.6", "Rose Likesom", 192))

for pub in pubs:
    pub.print_info()

#question 2

class car:
    def __init__(self, regnumb, maxspd):
        self.regnum = regnumb
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

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance


class ElectricCar(car):
    def __init__(self, regnumb, maxspd, battCap):
        super().__init__(regnumb, maxspd)
        self.battCap = battCap


class GasolineCar(car):
    def __init__(self, regnumb, maxspd, tankVol):
        super().__init__(regnumb, maxspd)
        self.tankVol = tankVol



newEcar = ElectricCar("ABC-15", 180, 52.5)
newEcar.accelerate(80)
newEcar.drive(3)
print(f"Electric car travelled: {newEcar.travelledDistance} km")
newGcar = GasolineCar("ACD-123", 165, 32.3)
newGcar.accelerate(120)
newGcar.drive(3)
print(f"Gasoline car travelled: {newGcar.travelledDistance} km")
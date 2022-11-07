#Exercise 10
#Question 1
class Elevator:
    def __init__(self, botton, top):
        self.botton = botton
        self.top = top
        self.current = botton

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current * 1}")
            self.current += 1
            return True

        else:
            return False

    def floor_down(self):
        if self.current > self.botton:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range (floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"You are already at this floor: {self.current}")

h = Elevator(1, 5)
target_floor = int(input("Which floor would you like to go to "))
h. go_to_floor(target_floor)
h.go_to_floor(1)

#Question 2

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current + 1}")
            self.current += 1
            return True

        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                if not self.floor_up():
                    break

        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"you are already at the floor {self.current}")


class Building:
    def __init__(self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_no, floor):
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)


print("Elevator in the building")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 5)
building.run_elevator(3, 2)

#question 3

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current + 1}")
            self.current += 1
            return True

        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                if not self.floor_up():
                    break

        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"You are already at the floor {self.current}")


class Building:
    def __init__(self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range (elevator_list):
            self.elevator_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_no, floor):
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)

    def fire_alarm(self):
        print("-------------------------------------")
        print("           !!!Fire!!!")
        for i in self.elevator_list:
            i.go_to_floor(i.bottom)


print("Elevator in the building")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 5)
building.run_elevator(3, 2)
building.fire_alarm()

#question 4

import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, acceleration):
        self.current_speed = min(max(self.current_speed + acceleration, 0), self.maximum_speed)

    def drive(self, time):
        self.travelled_distance += self.current_speed * time


class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        print("Plate  Speed Travelled Distance")
        print("------------------------------")
        for car in self.cars_list:
            print(f"{car.registration_number:6s}: {car.current_speed:3d}, {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars_list:
            if car.travelled_distance >= self.distance:
                return True
        return False


car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

race = Race("  Grand Demolition Derby", 8000, car_list)
n = 0
while not race.race_finished():
    race.hour_passes()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is: ")
race.print_status()










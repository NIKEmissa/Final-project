# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import queue
import time


# In[2]:

class car:
    def __init__(self, name='noNameCar'):
        self.name = name
        self.length = 2.5
        self.speed = 11.176
        self.acceleration = 0


# In[3]:

class traffic_light:
    def __init__(self):
        self.turnTime = 30
        self.Colors = ['G', 'R']


# In[4]:

class road:
    def __init__(self, length=3000):
        self.length = length
        self.cars = pd.DataFrame(
            index=['Length', 'Speed', 'Acceleration', 'CurrentLoc', 'RemainDis', 'NextLight', 'MoveTime', 'StopTime'])
        self.trafficLights = pd.DataFrame(index=['TurnTime', 'Colors', 'CurrentColor', 'Location'])

    def put_car(self, numCars=0):
        for i in range(numCars):
            temp = {}
            tempCar = car(i)
            temp['{}'.format(i)] = {'Length': tempCar.length, 'Speed': tempCar.speed,
                                    'Acceleration': tempCar.acceleration, 'CurrentLoc': 0, 'RemainDis': 1500,
                                    'NextLight': None, 'MoveTime': 0, 'StopTime': 0}
            temp = pd.DataFrame(temp)
            self.cars = self.cars.join(temp)
        self.number_of_cars = len(self.cars.columns)
        print(self.cars)

    def put_trafficLight(self, location=1000, lightName='noNameLight', turnTime=30):
        temp = {}
        tempLig = traffic_light()
        temp[lightName] = {'TurnTime': turnTime, 'Colors': tempLig.Colors, 'CurrentColor': 'G', 'Location': location}
        temp = pd.DataFrame(temp)
        self.trafficLights = self.trafficLights.join(temp)
        print(self.trafficLights)


# In[5]:

Green_road = road()

# In[7]:

Green_road.put_car(int(input('Please input how many cars you want to simulate:')))

# In[8]:

Green_road.put_trafficLight(lightName='0', turnTime=120, location=400)
Green_road.put_trafficLight(lightName='1', turnTime=120, location=700)
Green_road.put_trafficLight(lightName='2', turnTime=120, location=1400)

Green_road.put_trafficLight(lightName='7', turnTime=9999999, location=99999999)


# In[13]:

def which_light_next(car, lights):
    count = 0

    for i in range(len(lights.columns)):

        dist = car.CurrentLoc - lights.iloc[:, i].Location
        if dist < 0:
            if count == 0:
                last_dist = dist
                next_light = lights.iloc[:, i].name
                count += 1
            elif abs(last_dist) > abs(dist):
                last_dist = dist
                next_light = lights.iloc[:, i].name

    if count == 0:
        return None
        print('There is no next traffic light')
    else:
        return next_light


# In[15]:

def change_light_color(lights, time):
    for i in range(len(lights.columns)):
        if (time / 10) % lights.iloc[:, i].TurnTime == 0:  # time change
            lights.iloc[:, i].CurrentColor = list(set(lights.iloc[:, i].Colors) - set(lights.iloc[:, i].CurrentColor))


# In[18]:

def car_collison(cars, car_Num):
    if car_Num > 0:
        if (cars.iloc[:, car_Num - 1].CurrentLoc - cars.iloc[:, car_Num].CurrentLoc) >= 1.5:  # time change
            return False
        else:
            return True
    else:
        return False


for currentCS in range(100000):

    change_light_color(Green_road.trafficLights, currentCS)

    for carNum in range(len(Green_road.cars.columns)):
        car = Green_road.cars.iloc[:, carNum]
        car.NextLight = which_light_next(car, Green_road.trafficLights)
        nextLig = Green_road.trafficLights[str(int(car.NextLight))]

        if ((car.CurrentLoc + 1.1176 > nextLig.Location) & (nextLig.CurrentColor == ['R'])) \
                | car_collison(Green_road.cars, carNum):  # stop #time change
            # continue
            if (carNum == len(Green_road.cars.columns) - 1) | (carNum == 0):
                if car.RemainDis > 0:
                    print(' This is car #', '{0:0>3}'.format(str(carNum)), '\n', 'The remaining distance:',
                          '{0:*>10,.4f}'.format(car.RemainDis), '  ', 'The car is stop')

        else:  # keep running

            car.CurrentLoc = car.MoveTime * (car.Speed / 10)  # time change
            car.RemainDis = 1500 - car.CurrentLoc
            if (carNum == len(Green_road.cars.columns) - 1) | (carNum == 0):
                if car.RemainDis > 0:
                    print(' This is car #', '{0:0>3}'.format(str(carNum)), '\n', 'The remaining distance:',
                          '{0:*>10,.4f}'.format(car.RemainDis), '  ', 'The car is running')
            car.MoveTime += 1

    if Green_road.cars.iloc[:, len(Green_road.cars.columns) - 1].RemainDis < 0:
        print(' The Last car is gone')
        break

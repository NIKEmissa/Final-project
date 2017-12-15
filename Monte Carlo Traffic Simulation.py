#variable : each car's speed . lights turning time.

# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import queue
import time


# In[2]:

class car:
    """
    Define a class named car, it contains car's name, car's length and car's speed.
    >>> carA = car('Tesla')
    >>> carA.name
    Tesla
    >>> car.carA.length
    2.5
    """

    def __init__(self, name='noNameCar'):
        self.name = name
        self.length = 2.5
        self.speed = 10.3 + float(np.random.beta(6, 2, 1))


class traffic_light:
    """
    >>> tlA=traffic_light()
    >>> print(tlA.turnTime)
    30
    >>> print(tlA.Colors)
    ['G', 'R']
    """
    def __init__(self):
        self.turnTime = int(np.random.uniform(40, 60, 1))
        self.Colors = ['G', 'R']



class road:
    def __init__(self, length=3000):
        self.length = length
        self.cars = pd.DataFrame(
            index=['Length', 'Speed', 'CurrentLoc', 'RemainDis', 'NextLight', 'MoveTime', 'StopTime',\
                   'TotalTime'])
        self.trafficLights = pd.DataFrame(index=['TurnTime', 'Colors', 'CurrentColor', 'Location'])

    def put_car(self, numCars=0):
        '''
        :param numCars: The number of the cars the user
        :return: A dataframe contains all the index about the cars. For example, if we put one car, it will
                has the car's  'Length', 'Speed', 'CurrentLoc', 'RemainDis', 'NextLight', 'MoveTime', 'StopTime'.
                The initial value for all car will be same.

        '''

        for i in range(numCars):
            # initial a dictionary.
            temp = {}
            tempCar = car(i)
            #Add car's index and value into dictionary.
            temp['{}'.format(i)] = {'Length': tempCar.length, 'Speed': tempCar.speed,
                                    'CurrentLoc': 0, 'RemainDis': 1500,
                                    'NextLight': None, 'MoveTime': 0, 'StopTime': 0,'TotalTime':0}
            #convert into dataframe.
            temp = pd.DataFrame(temp)
            self.cars = self.cars.join(temp)
        self.number_of_cars = len(self.cars.columns)

    def put_trafficLight(self, location=1000, lightName='noNameLight', turnTime=30):
        '''
        :param location: The location for the trifficlight and initial value is 1000m.
        :param lightName: The name of the trifficlight.
        :param turnTime: The turning time of the trifficlight.
        :return: A dataframe contains all the index about the trifficlight.
        '''

        # initial a dictionary.
        temp = {}
        tempLig = traffic_light()

        # Add trafficlight's index and value into dictionary.
        temp[lightName] = {'TurnTime': tempLig.turnTime, 'Colors': tempLig.Colors, 'CurrentColor': 'G', 'Location': location}

        # convert into dataframe.
        temp = pd.DataFrame(temp)
        self.trafficLights = self.trafficLights.join(temp)




# initial a road.
Green_road = road()

# User input the number of the car.
Green_road.put_car(int(input('Please input how many cars you want to simulate:')))

# set the locations of the trafficlights.
Green_road.put_trafficLight(lightName='0', location=400)
Green_road.put_trafficLight(lightName='1', location=700)
Green_road.put_trafficLight(lightName='2', location=1400)

# set a dummy trafficlight.
Green_road.put_trafficLight(lightName='7', turnTime=9999999, location=99999999)


def which_light_next(car, lights):
    '''
    :param location: The location for the trifficlight and initial value is 1000m.
    :param lightName: The name of the trifficlight.
    :param turnTime: The turning time of the trifficlight.
    :return: A dataframe contains all the index about the trifficlight.
    '''

    count = 0

    for i in range(len(lights.columns)):

        # get the distance between car and light.
        dist = car.CurrentLoc - lights.iloc[:, i].Location

        # if dist is negative, the car has not reached the trifficlight.
        if dist < 0:

            # If there is not any triffic light in the front of the car.
            if count == 0:
                last_dist = dist
                next_light = lights.iloc[:, i].name
                count += 1

            # If there is any triffic light in the front of the car.
            elif abs(last_dist) > abs(dist):
                last_dist = dist
                next_light = lights.iloc[:, i].name

    if count == 0:
        return None
        print('There is no next traffic light')
    else:
        return next_light



def change_light_color(lights, time):
    '''
    :param lights: The dataframe of all triffic light together.
    :param time: The time begins when the first car came in and by now.
    :return:
    '''
    #This is a function to control when to change the color.
    for i in range(len(lights.columns)):

        # If now is turning time.
        if (time / 10) % lights.iloc[:, i].TurnTime == 0:  # time change

            # change the current color.
            lights.iloc[:, i].CurrentColor = list(set(lights.iloc[:, i].Colors) - set(lights.iloc[:, i].CurrentColor))



def car_collison(cars, car_Num):
    '''
    :param cars: The dataframe of all cars together.
    :param car_Num: The number of the cars.
    :return: If the car can keep going for another second or not.
    '''

    if car_Num > 0:
        # If the distance between two cars is longer than 2M, the back car won't stop.
        if (cars.iloc[:, car_Num - 1].CurrentLoc - cars.iloc[:, car_Num].CurrentLoc) >= 2:  # time change
            return False
        else:
            return True
    else:
        return False



# simulate the time flow, it's unit is millisecond.
for currentCS in range(100000):

    # control the lights' color.
    change_light_color(Green_road.trafficLights, currentCS)

    # control each car's movement.
    for carNum in range(len(Green_road.cars.columns)):
        car = Green_road.cars.iloc[:, carNum]

        # Decide the next light.
        car.NextLight = which_light_next(car, Green_road.trafficLights)
        nextLig = Green_road.trafficLights[str(int(car.NextLight))]

        # Decide if the car will reach the triffic light and if the triffic light is RED, the car will stop.
        if ((car.CurrentLoc + (car.Speed/10) > nextLig.Location) & (nextLig.CurrentColor == ['R'])) \
                | car_collison(Green_road.cars, carNum):  # stop #time change

            # Output the first and the last car's movement information.
            if (carNum == len(Green_road.cars.columns) - 1) | (carNum == 0):

                # if the car still is in the road, then output the car's information.
                if car.RemainDis > 0:
                    print(' This is car #', '{0:0>3}'.format(str(carNum)), '\n', 'The remaining distance:',
                          '{0:>10,.4f}'.format(car.RemainDis), '  ', 'The car is stop')
            if car.CurrentLoc > 0:
                car.StopTime += 0.1

        else:  # keep running

            car.CurrentLoc += (car.Speed / 10)  # time change

            # The rest distance.
            car.RemainDis = 1500 - car.CurrentLoc

            # Output the first and the last car's movement information.
            if (carNum == len(Green_road.cars.columns) - 1) | (carNum == 0):

                # if the car still is in the road, then output the car's information.
                if car.RemainDis > 0:
                    print(' This is car #', '{0:0>3}'.format(str(carNum)), '\n', 'The remaining distance:',
                          '{0:>10,.4f}'.format(car.RemainDis), '  ', 'The car is running')
            if car.RemainDis > 0:
                car.MoveTime += 0.1

    # If the remian distance is negative, the car was leaving the road.
    if Green_road.cars.iloc[:, len(Green_road.cars.columns) - 1].RemainDis < 0:
        print(' The Last car is gone')
        break

# Calculate the total time of each car.
for carNum in range(len(Green_road.cars.columns)):
    car = Green_road.cars.iloc[:, carNum]
    car.TotalTime = car.MoveTime + car.StopTime

#Calculate the average time of each car.
TTmean = Green_road.cars.loc['TotalTime'].mean()
print(Green_road.cars,'\n',Green_road.trafficLights,'\n','The average total time is {0:>10,.4f} seconds.'.format(TTmean))
# Title: Traffic Simulation by Using Monte Carlo Simulation

# Github link: https://github.com/NIKEmissa/Final-project

## Team Member(s): Xingxing Zhang, Xinzhe Deng

# Monte Carlo Simulation Scenario & Purpose:
  In urban planning, it is rather important to determine the traffic volume in each road. In order to control the traffic volume, we need to control the each traffic light’s turning-time to make the most reasonable plan for each traffic light on the road.
  Based on the actual situation, we are developing a traffic model to simulate the traffics’ movements in a certain road which contains a few crossroads (traffic lights).  The purpose of this simulation is to examine the average passing time for each car by changing the traffic lights’ turning-time. In the end, not only we will find the shortest passing time for the car but we can make reasonable decision to control the traffic volume as we want.

### Hypothesis before running the simulation:
1.The total length of chosen road is setted to 3 kilometers from the start-point to the end-point. 
2.The road is a straight asphalt road.
3.The number of traffic lights under this scenario is setted to 3. 
4.The distances between two adjacent traffic lights are 600m and 1000m, respectively.
5.We are not going to take Yellow light into consideration. Thus, in this scenario, the traffic lights only have red and green lights.
6.The highest speed of cars is 30 miles/hours. We assume that the cars keep the highest speed except when they are accelerating and slowing down.
7.The people’s ‘reaction time to the changing light is not taken into consideration. We assume that drivers will speed up as long as they see traffic light changing.

### Simulation's variables of uncertainty
  We have three variables of uncertainty. 
  We consider three traffic lights in a certain road so that each traffic light is an variables because each traffic light has its individuel turning-time.
  For each traffic lights we set the range of turning-time is from 35 seconds to 120 seconds which is random distribution.
We think it will be a good representation of reality because the variables and the time range are also selected from reality and also we combine the green light and yellow light to simulate the situation that some people always try to jump a yellow light.

## Instructions on how to use the program:
Users are allowed to input customized values for the switching-time between green lights and red lights as well as the distances between traffic lights. Or, users can use the default values of the parameters. If users choose the pre-set values, program will run Monte Carlo simulations after users start it and output final result of the total time to go through three traffic lights.

## Sources Used:
Traffic light control and coordination: https://en.wikipedia.org/wiki/Traffic_light_control_and_coordination


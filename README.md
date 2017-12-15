# Title: Traffic Simulation by Using Monte Carlo Simulation

# Github link: https://github.com/NIKEmissa/Final-project

## Team Member(s): Xingxing Zhang, Xinzhe Deng

# Monte Carlo Simulation Scenario & Purpose:
  In urban planning, it is rather important to determine the traffic volume in each road. In order to control the traffic volume, we need to control the each traffic light’s turning-time to make the most reasonable plan for each traffic light on the road.
  
  Based on the actual situation, we are developing a traffic model to simulate the traffics’ movements in a certain road which contains a few crossroads (traffic lights).  The purpose of this simulation is to examine the average passing time for each car by changing the traffic lights’ turning-time. In the end, we will know in different amount of cars in the road, the average time to passing the road which means we may can find that if the limited speed is reasonable.
  
  Firstly, we randomly give plenty of cars (user input) running on the same road. Then, we would let cars start to run from the start point one by one. We would use uniform distribution to allocate time intervals for every two cars. When the simulation is over, we would see how much time is spent on each car to complete this journey. The timer starts from the first car comes in and terminates after the last car comes out. The total time for every vehicle to finish the journey we call it the capability of a road to consume cars.

  In all of our simulations, the final goal is finding the relationship between the time consuming, the traffic lights’ changing time, the speed of each car and the number of cars. And we want to find out how long it will take to finish the simulation when we allocate the different turning time to different traffic lights.
  
  In order to get the average time consumption, we would run several times for each scenario and then calculate the average time using total time dividing the times we run the simulation.

### Hypothesis before running the simulation:
1.The total length of chosen road is setted to 1.5 kilometers from the start-point to the end-point. 

2.The road is a straight asphalt road.

3.The number of traffic lights under this scenario is setted to 3.

4.In the selected road, we put these three trffic lights at the locations of 400m, 700M, 1400m.

5.We are not going to take Yellow light into consideration. Thus, in this scenario, the traffic lights only have red and green lights.

6.The limited speed of the road is 25 miles/hours which is 11.176m/s. We assume that the cars' speed will follow a normal distrubution.

7.We set the turning time of triffic lights follow the uniform distrubution.

### Simulation's variables of uncertainty
  We have three variables of uncertainty.
  1. The turning-time of each traffic light.
  We consider three traffic lights in a certain road so that each traffic light is an variables because each traffic light has its individuel turning-time. We use the way of Monte Carlo to simulate the turning time of each trffic light from 30 seconds to 120 seconds and each turning time will fellow random distribution.
  
 2. Each car’s speed.
  We use the way of Monte Carlo to simulate each car's speed, we set the speed about 25 mile per hour and it fellow the normal distrubution. And because lots of people will drive a little faster than the limited speed, the distrubution is left skew.
  
  3. The number of cars.
  We will let the user to input as many cars as they want.
  
  We think it will be a good representation of reality because the variables and the time range are also selected from reality and also we combine the green light and yellow light to simulate the situation that some people always try to jump a yellow light.

## Instructions on how to use the program:
  Users are allowed to input customized values for the amount of the cars, then the program will calculate each car's remaining distance and the car's status, program will keep output the first car’s information and the last one’s information. Users can see how many distance that still remains for the cars. In the end, it will users can see the summaries for the cars and the lights. Also, the average total time spent on the selected road can be saw.

## Sources Used:
Traffic light control and coordination: https://en.wikipedia.org/wiki/Traffic_light_control_and_coordination

The normal distrubution: https://en.wikipedia.org/wiki/Normal_distribution

The Uniform distrubution: https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)

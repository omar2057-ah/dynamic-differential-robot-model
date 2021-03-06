# -*- coding: utf-8 -*-
"""Dynamic Differential Robot Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rd7XetYhc9gEdWqVUcMq7olXag_1OxNu
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Diff_Robot():
    def __init__(self):
        self.xc = 2
        self.yc = 3
        self.xdot = 0
        self.thetadot = 0
        self.theta = np.pi/2
        self.r = 1  #radius of Wheel
        self.L = 2   # distance between wheels
        self.m = 1    # Mass of robot
        self.J = 4    # Robot Inertia
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
 
class Diff_Robot(Diff_Robot):
    def step(self, Tl, Tr):
            
            XDoubledot = (Tr+Tl)/(self.m*self.r)
            ThetaDoubledot = (Tr - Tl)*self.L/(2*self.r*self.J)
            self.xdot = self.xdot + XDoubledot*self.sample_time
            self.thetadot = self.thetadot + ThetaDoubledot*self.sample_time
            Vx = self.xdot*np.cos(self.theta)
            Vy = self.xdot*np.sin(self.theta)
            self.xc = self.xc + Vx*self.sample_time
            self.yc = self.yc + Vy*self.sample_time
            self.theta = self.theta + self.thetadot*self.sample_time
            
 
             
            pass

sample_time = 0.01
time_end = 120
model = Diff_Robot()
 
t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)
theta_data = np.zeros_like(t_data)
xdot_data = np.zeros_like(t_data)
 
for i in range(t_data.shape[0]):
    x_data[i] = model.xc
    y_data[i] = model.yc
    theta_data[i] = model.theta
    xdot_data[i] = model.xdot*np.sin(model.theta)
 
    model.step(0.02, 0.01)

#plt.axis('equal')
plt.plot(t_data, x_data,label='Dynamic Differential Model - x data')
plt.legend()
plt.grid()
plt.show()
plt.plot(t_data, y_data,label='Dynamic Differential Model - y data')
plt.legend()
plt.grid()
plt.show()
plt.plot(t_data, theta_data,label='Dynamic Differential Model - theta data')
plt.legend()
plt.grid()
plt.show()
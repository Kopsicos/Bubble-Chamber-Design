# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:53:15 2020

@author: Sasha Alexander Viktorovich Korol
"""
# Physics Project

# Make everything 2d
# Two distance variables (x,y)

#x = vx*time + x0 <- x0 = 0
#y = vy*time + y0 <- y0 = 0
# RNG for y position

import random
import matplotlib.pyplot as plt
import numpy as np # How to draw spirals

class Particles:
    def __init__(self, charge, velocity, trajectories=None):
        """
        Initializes the Particle class
        """
        self.charge = charge
#        self.mass = mass
        self.velocity = velocity
        self.trajectories = trajectories

class Beam:
    def __init__(self, rad, leng, time, strength):
        self.rad = rad
        self.leng = leng
        self.time = time
        self.strength = strength
        
    def shoot_particles(self, particles):
        plt.figure("particle trajectory")
        plt.title("particle trajectory")
        time = np.linspace(0, self.time, 10)
        for particle in particles:
            plt.plot(time, particle.velocity*time)
            plt.xlabel('x')
            plt.ylabel('y')
        plt.legend()
        plt.show()
    
    def particle_behavior(self, particles):
        plt.figure("particle behavior")
        plt.title("particle behavior")
        theta = np.radians(np.linspace(1000,random.randint(90,1440)*5,1000))
        r = theta**3
        x_2 = r*np.cos(theta)
        y_2 = r*np.sin(theta)
        time = np.linspace(0, self.time, 1000)
        for particle in particles: #Use random number generator
            plt.xlabel('time')
            plt.plot(x_2,y_2)
            plt.plot(time, np.piecewise(time, [time == 2, time != 2], [0, 1]))

            plt.ylabel('distance')
            plt.show()
        
#time, np.piecewise(r, [x_2, y_2], [0, 1]
#    self.strength*particle.velocity*np.sin(time)
part_list = [Particles(i+1,3) for i in range(1)] # Use RNG to determine starting position

Bm = Beam(10, 10, 10, 14)
Bm.shoot_particles(part_list)
Bm.particle_behavior(part_list)
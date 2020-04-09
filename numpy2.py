# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:23:36 2020

@author: Sasha Alexander Viktorovich Korol
"""
# Two coordinates
# t = time


import numpy as np
x = np.arange(0., 5., 0.2)
import matplotlib.pyplot as plt
import random
print(random.randint(0, 5))
plt.plot(x, np.piecewise(x*2, [x == 2, x != 2], [0, 1]))

#fig = plt.figure()
#ax=fig.add_subplot(1)

def ypos():
    ypos = (random.randint(0, 20))
    return ypos

def movement(time, b):
    return (time) + b
   
def exp(time):
    return (1/100)*np.exp(time)

# Piecewise combine with spirals
# Basic Properties of particles

theta = np.radians(np.linspace(1000,360*5,1000))
r = theta**3
x_2 = r*np.cos(theta)
y_2 = r*np.sin(theta)
plt.figure(figsize=[5,5])
plt.plot(x_2,y_2)
#plt.show()

y = np.linspace(-2.5, 2.5, 6)
plt.plot(x_2,np.piecewise(y_2, [x_2 < 0,x_2 >= 0], [lambda x_2: -x_2, lambda x_2: x_2]))
plt.plot(x_2,np.piecewise(y_2, [y_2 < 0,y_2 >= 0], [lambda x_2: -x_2, lambda x_2: x_2]))
#plt.plot(x_2,np.piecewise(y_2, [y_2 < 0,y_2 >= 0], [lambda x_2: -x_2, lambda x_2: x_2]))

#time_lst = np.linspace(0, 10, 10)
#z = np.array(movement(time_lst, ypos()))
#
#plt.figure("first Graph")
#plt.title("first Graph")
#plt.plot(time_lst, z, linestyle=None, marker='.')
#plt.show()
#plt.plot(time_2nd, np.sin(angles) + z[-1], linestyle=None, marker='.')
#
#for i in range(10):
#   plt.show()
#x = y = np.linspace(0, 5*5, 1)
#plt.plot(x, ypos(), label='particle behavior', color = 'red')
#plt.plot(y, x*-1, label = "second Plot", color = "purple")
#plt.plot(y, x*-1-1, label = "third Plot", color = "black")
#plt.show()

#a = np.array([[1,2,4], [5,8,7]], dtype = "float")
#print("Array created using passed list: \n", a)
#
#b = np.array((1,3,2))
#print ("\nArray created using passed tuple: \n", b)
#
#c = np.zeros((3,4))
#print("\nAn array initialized with all zeros: \n", c)
#
#d = np.full((3,3), 6, dtype = "complex")
#
#e = np.random.random((2,2,))
#print("\nA random array: \n", e)
#
#f = np.arange(0,30,5)

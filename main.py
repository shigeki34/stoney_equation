#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using storny equation, this program calculates strain in thin film on substrate


"""
import matplotlib.pyplot as plt
import numpy as np

n = 5
eps = 1e-3
deriv = np.zeros((n,n), float)
f = np.zeros((n), float)
# L0, h0 are already know, input data [mm]
L0 = 100
h0 = 0.02
# R0 is rough estimation. theta is small enough and supposed theta = sin(theta)
R0 = (L0**2 / 4.0 + h0**2)/(2.0*h0)
d0 = L0
theta0 = L0/(2.0*R0)

x = np.array([L0, d0, h0, R0, theta0])

def F(x, f):
    f[0] = x[0] - 2.0*x[3]*x[4]
    f[1] = x[1] - 2.0*x[3]*np.sin(x[4])
    f[2] = x[2] - x[3]*(1.0-np.cos(x[4]))
    f[3] = x[0] - L0
    f[4] = x[2] - h0

def dFi_dXj(x, deriv, n):
    h = 1e-4
    for j in range(0, n):
        temp = x[j]
        x[j] = x[j] + h/2
        F(x, f)
        for i in range(0, n):
            deriv[i, j] = f[i]
        x[j] = temp
    for j in range(0, n):
        temp = x[j]
        x[j] = x[j] - h/2
        F(x, f)
        for i in range(0, n):
            deriv[i, j] = (deriv[i, j]- f[i])/h
        x[j] = temp

for it in range(1, 100):
    F(x, f)
    dFi_dXj(x, deriv, n)
    B = np.array([[-f[0]], [-f[1]], [-f[2]], [-f[3]], [-f[4]]])
    sol = np.linalg.solve(deriv, B)
    dx = np.take(sol, (0, ), 1)
    for i in range(0, n):
        x[i] = x[i] + dx[i]
    errX = errF = errXi = 0.0
    for i in range(0, n):
        if(x[i] != 0.0):
            errXi = abs(dx[i]/x[i])
        else:
            errXi = abs(dx[i])
        if(errXi > errX):
            errX = errXi
        if(abs(f[i]) > errF):
            errF = abs(f[i])
        if((errX <= eps) and (errF <= eps)):
            break

print('Number of iterations = ', it, "\n Final Solution:")
for i in range(0, n):
    print('x[', i,'] = ', x[i])

#Elastic modulus rate [GPa]
E_SiC = 748
E_GaN = 150
E_AlN = 308

#Poisson ratio
nu_SiC = 0.21
nu_GaN = 0.23
nu_AlN = 0.287

#Choose Substrate material
E_sub = E_SiC
nu_sub = nu_SiC

#Thickness of substrate and film [mm]
t_sub = 0.5
t_film = 0.0005 # 500nm => 5e-4mm

#strain
sigma = (E_sub * t_sub**2)/(6*(1.0-nu_sub)*x[3]*t_film)

print('strain in film:', sigma, '[GPa]')

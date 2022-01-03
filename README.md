# stoney_equation
Calculate radius of curvature and residual stress of thin film using stoney's equation

Residual strain of thin film which is deposited on substrate is one of the most interesting properties.
However, it is difficult to measure directly and we evaluate from radius curvature.
This program can help you to calcurate.

# Calcurate radius of curvature
At first, we calcurate radius of curvature.  
Fig. 1 shows the parameters of this calcuration.  
We use 5 parameters;

L: diameter of substrate  
d: length of chord  
h: height  
R: radius of curvature  
Θ: angle  

![Fig1](images/fig1.png)

Ver 1.0  
We need exact data of L and h for calcurate.
I hope you probably know the both parameter when you want to calcurate residual strain.

# Stoney Equation
Stoney Equation is as shown below.

<img src="https://latex.codecogs.com/svg.image?\sigma&space;=&space;\frac{E_{s}t_{s}^{2}}{6(1-\nu&space;_{s})Rt_{f}}" title="\sigma = \frac{E_{s}t_{s}^{2}}{6(1-\nu _{s})Rt_{f}}" />

where the subscripts s and f refer to substrate and film variables, Es is the elastic modulus for the substrate, t is the thickness, R is the radius of curvature, and ν is Poisson’s ratio.

Elastic modulus and Poisson's ratio are here.

| | SiC | GaN | AlN |
| :-- | :-: | :-: | :-: |
|elastic modulus (GPa) |  | td | td |
|Poisson's ratio |  | td | td |


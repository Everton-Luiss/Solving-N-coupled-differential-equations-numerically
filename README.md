## Solving a set of N coupled differential equations
In the daily life of a scientist it is usual to come across with second order diferential equations. If you are here then you probably have a second order differential equation to solve. I hope that this program can help you!
### Usage example 
This program is able to solve a set of **N** first order differential coupled equations, but in order to illustrate how it works we consider a simple example of just **N = 2** coupled equations. The case discussed here is the simple harmonic oscillator. For this example you must follow the following steps:
- **Step 1:** Convert your second order differenttial equation into a set of two ordinary differential equations. In the image bellow I illustrate this procedure considering the harmonic oscillator case
***
![diff](https://user-images.githubusercontent.com/68023745/87543533-4dfe2600-c67b-11ea-8f7f-ba12782bfe4b.png)

Identify the variables you are using. In the case we present here the two variables are the position (**x**) and velocity (**v**) of the oscillator. The first position  derivative is the velocity and the first velocity derivative is the acceleration.
- **Step 2:** In order to put this equations into the program you must follow the notation: for variables you use **y[argument]** and for derivatives you use **yp[argument]**. The argument of the **y** function is a number that labels each one of the system variables. See the following figure to clarify: 
***
![diff2](https://user-images.githubusercontent.com/68023745/87547417-72f59780-c681-11ea-99d5-09a82cb68d16.png)

To see how it is written into program [click here](https://github.com/Everton-Luiss/Resolvendo-N-equacoes-Diferenciais/blob/master/sub.c).

-**Step 3:** Set the initial conditions. When you run the program it will ask to you the initial conditions.

-**Step 4:** Be happy! Your problems are now solved!

### How it works?
To solve the set of diferrential equations we used the fourth order Runge-Kutta method. This method finds approximate value of **x** for a given time **t**. Only first order ordinary differential equations can be solved by using the Runge Kutta 4th order method. To learn more about the Runge-Kutta method [click here](https://pt.wikipedia.org/wiki/M%C3%A9todo_de_Runge-Kutta).

### Problems?
If you find any issue, please report it.
***
Desenvolvido por Everton Silva

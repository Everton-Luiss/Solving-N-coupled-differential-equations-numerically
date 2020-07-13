#include <stdio.h>
#include <math.h>

void  f(double x,double *y, double *yp)
    {
    yp[0]=y[1];
    yp[1]=-0.2*y[0];
    }
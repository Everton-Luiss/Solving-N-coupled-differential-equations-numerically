#include <stdio.h>
#include <math.h>
#include "sub.c"

#define N 2
#define dist 0.01
#define MAX 30.0

void main()
{
FILE *output, *out;
double x, y[N], S, V;
int j;

output = fopen("numerico.dat", "w");
//out=fopen("analitico.dat", "w");

printf("Type initial position: ");
scanf("%lf", &S);

printf("Type initial velocity: ");
scanf("%lf", &V);
//printf("How many coupled equations?: ")
	
S = y[0];
V = y[1];
fprintf(output, "0\t%f\n", y[0]);

for (j=1; j*dist<=MAX ;j++)
{
   x=j*dist;
   runge4(x, y, dist);

   fprintf(output, "%f\t%f\n", x, y[0]);
   //fprintf(out, "%lf %lf\n",x, 2.0*cos(sqrt(0.2)*x));
  
}

fclose(output);
//fclose(out);
}

void runge4( double x, double *y, double step)
{
double c1[N],c2[N],c3[N],c4[N],yy[N],h2=step/2.0;
int i;

	f(x, y,c1);
        for (i=0; i<N; i++) yy[i]=y[i]+h2*c1[i];
        f(x+h2,yy,c2);
        for (i=0; i<N; i++) yy[i]=y[i]+h2*c2[i];
        f(x+h2,yy,c3);
        for (i=0; i<N; i++) yy[i]=y[i]+step*c3[i];
        f(x+dist,yy,c4);
        for (i=0; i<N; i++)
          y[i]+=step*(c1[i]+2.0*c2[i]+2.0*c3[i]+c4[i])/6.0;

}
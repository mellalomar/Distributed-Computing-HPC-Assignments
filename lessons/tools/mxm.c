#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int n = 1000;

    double** a;
    double** b;
    double** c;

    srand(time(NULL));

    a =(double **)malloc(n*sizeof(double *));
    a[0] = (double *)malloc(n*n*sizeof(double));
    
    if(!a)
    {
        printf("memory failed \n");
        exit(1);
    }
    for(int i=1; i<n; i++)
    {
        a[i] = a[0]+i*n;
        if (!a[i])
        {
            printf("memory failed \n");
            exit(1);
        }
    }

    
    b =(double **)malloc(n*sizeof(double *));
    b[0] = (double *)malloc(n*n*sizeof(double));
    
    if(!b)
    {
        printf("memory failed \n");
        exit(1);
    }
    for(int i=1; i<n; i++)
    {
        b[i] = b[0]+i*n;
        if (!b[i])
        {
            printf("memory failed \n");
            exit(1);
        }
    }
    
    c =(double **)malloc(n*sizeof(double *));
    c[0] = (double *)malloc(n*n*sizeof(double));
    
    if(!c)
    {
        printf("memory failed \n");
        exit(1);
    }
    for(int i=1; i<n; i++)
    {
        c[i] = c[0]+i*n;
        if (!c[i])
        {
            printf("memory failed \n");
            exit(1);
        }
    }
    
    // initialize the matrices
    for(int i=0; i<n; i++)
      {
        for(int j=0; j<n; j++)
	  {
            a[i][j] = 1. + rand()%100;
            b[i][j] = 2. + rand()%100;
	    c[i][j] = 0.;
	  }
      }

    
    
    //basic multiplication matrices
    double start = (double)clock() /(double) CLOCKS_PER_SEC;

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n ; j++)
	for (int k = 0; k < n ; k++)
	  c[i][j] += a[i][k]* b[k][j];

    double end = (double)clock() / (double) CLOCKS_PER_SEC;
    double msec =  (end - start) * 1000.;
    double rate = sizeof(double) * (2*n*n) * (1000.0 / msec) / (1024*1024);
    printf("baseline_matrix_multiply %fs , rate %f\n",msec, rate);



    //flip jk multiply matrices
    start = (double)clock() /(double) CLOCKS_PER_SEC;
    
    for (int i = 0; i < n; i++)
      for (int k = 0; k < n ; k++)
	for (int j = 0; j < n ; j++)
	  c[i][j] += a[i][k]* b[k][j];

    end = (double)clock() / (double) CLOCKS_PER_SEC;
    msec =  (end - start) * 1000.;
    rate = sizeof(double) * (2*n*n) * (1000.0 / msec) / (1024*1024);
    printf("baseline_matrix_multiply_flipjk %fs , rate %f\n",msec, rate);
    
   
    //block multiply matrices
    int B = 0;
    printf("Entrer blocsize : ");
    scanf("%d", &B);
  
    start = (double)clock() /(double) CLOCKS_PER_SEC;

    double s = 0;
    for (int kk = 0; kk < n ; kk+=B)
      for (int jj = 0; jj < n ; jj+=B)
	for (int i = 0; i < n ; i++)
	  for (int j = jj; j < jj + B; j++)
	    {
	      s = c[i][j];
	      for (int k = kk; k <kk + B; k++)
		s += a[i][k] * b[k][j];
	      c[i][j] = s;
	    }
	    

    end = (double)clock() / (double) CLOCKS_PER_SEC;
     msec =  (end - start) * 1000.;
    
    rate = sizeof(double) * (2*n*n) * (1000.0 / msec) / (1024*1024);
    printf("fast_matrix_multiply_blocking %fs , rate %f\n",msec, rate);

    
    return 0;
}

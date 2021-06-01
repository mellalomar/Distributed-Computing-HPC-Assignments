import numpy as np
import time
from numba import njit

MAX_STRIDE = 10
SEED = 86456

N = 100000
a = np.zeros(N*MAX_STRIDE, dtype=np.double);
np.random.seed(SEED)

#@njit
def init_a():
    for i in range(N*MAX_STRIDE):
        a[i] = np.random.rand() + 1.0
    return a

a = init_a()
  
print("stride , mean, time (msec), rate (MB/s)\n"); 
@njit
def compute_mean(mean):
    for i in range(0, N*i_stride, i_stride):
            mean = mean + a[i];
    return mean



for i_stride in range(1,MAX_STRIDE):
    mean = 0.0

    start=time.time()
    mean = compute_mean(mean)
    end=time.time()
    
    msec = (end-start) * 1000.0; # time in milli-second;
    rate = 8 * N * (1000.0 / msec) / (1024*1024);
    
    print(i_stride, mean, msec, rate)
 
        
  #  printf("%d, %f, %f, %f,\n", i_stride, mean, msec, rate);

    
#  for (int i_stride = 1; i_stride < MAX_STRIDE+1; i_stride++)
#{
#  mean = 0.0;
#  start = (double)clock() /(double) CLOCKS_PER_SEC;
#  
#  for (int i = 0; i < N*i_stride; i+=i_stride)
#	mean = mean + a[i];    
#  
#  end = (double)clock() / (double) CLOCKS_PER_SEC;
#  mean = mean / N;
#
#  msec = (end-start) * 1000.0; // time in milli-second;
#  rate = sizeof(double) * N * (1000.0 / msec) / (1024*1024);
#	
#  printf("%d, %f, %f, %f,\n", i_stride, mean, msec, rate);

from numba import njit
import numpy as np

@njit
def baseline_matrix_multiply(a, b, n):
    '''
    baseline multiply
    '''
    c = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

@njit
def baseline_matrix_multiply_flipjk(a, b, n):
    '''
    same as baseline but switch j and k loops
    '''
    c = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        ci = c[i]
        for k in range(n):
            bk = b[k]
            aik = a[i][k]
            for j in range(n):
                ci[j] += aik * bk[j]
    return c

@njit
def fast_matrix_multiply_blocking(a, b, n, block):
    '''
    use blocking
    '''
    c = np.zeros((n, n), dtype=np.double)
    en = int(block * n/block)

    for kk in range(0, en, block):
        for jj in range(0, en, block):
            for i in range(n):
                for j in range(jj, jj + block):
                    s = c[i][j]
                    for k in range(kk, kk + block):
                        s += a[i][k] * b[k][j]
                    c[i][j] = s
    return c

import time

n = int(input("Entrer n\n"))
a = np.ones((n, n), dtype=np.double)
b = 2*np.ones((n, n), dtype=np.double)
start_time=time.time()
baseline_matrix_multiply(a,b,n)
msec = (time.time()-start_time)* 1000
rate = 8 * (2*n*n) * (1000.0 / msec) / (1024*1024);
print("baseline_matrix_multiply: "+str(msec), "rate", rate)

a = np.ones((n, n), dtype=np.double)
b = 2*np.ones((n, n), dtype=np.double)
start_time=time.time()
baseline_matrix_multiply_flipjk(a,b,n)
msec = (time.time()-start_time)* 1000
rate = 8 * (2*n*n) * (1000.0 / msec) / (1024*1024);
print("baseline_matrix_multiply_flipjk: "+str(msec), "rate", rate)


block = input("entrer le nombre de bloc : \n")
a = np.ones((n, n), dtype=np.double)
b = 2*np.ones((n, n), dtype=np.double)
start_time=time.time()
fast_matrix_multiply_blocking(a,b,n, int(block))
msec = (time.time()-start_time)* 1000
rate = 8 * (2*n*n) * (1000.0 / msec) / (1024*1024);
print("fast_matrix_multiply_blocking: "+str(msec), "rate", rate)







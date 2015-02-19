#! /bin/env python

import cmath
import numpy as np
import sys

def FFT(y):
    N = len(y)
    if N > 1 and N % 2 > 0:
        raise ValueError("gimme a power of 2!")
    if N <= 1: 
        return y
    else:
        even = FFT(y[0::2])
        odd =  FFT(y[1::2])
        T = [cmath.exp(-2j * cmath.pi * k/N) * odd[k] for k in xrange(N/2)]
        return [even[k] + T[k] for k in xrange(N/2)] + [even[k] - T[k] for k in xrange(N/2)]

if __name__=="__main__":
    import thinkdsp as dsp
    import matplotlib.pyplot as plt
    y = dsp.SawtoothSignal().make_wave().ys[:2048]
    fft = FFT(y)
    ts = [i for i in xrange(len(fft))]
    plt.plot(ts, fft)
    plt.show()

    

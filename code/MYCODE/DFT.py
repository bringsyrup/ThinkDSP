#! /bin/env python
import matplotlib.pyplot as plt
import numpy as np
import thinkdsp as dsp

def DFT(y):
    N = len(y)
    dft = [complex(0)] * N
    for k in range(N):
        s = complex(0) 
        for t in range(N):
            s += y[t] * np.exp(-2j * np.pi * t * k / N)
        dft[k] = s
    return dft

def dspDFT(y):
    N = len(y)
    ts = np.arange(N) / N
    freqs = np.arange(N)
    args = np.outer(ts, freqs)
    M = np.exp(2j * np.pi * args)
    amps = M.conj().transpose().dot(y)
    return amps

def npdft(y):
    return np.fft.fft(y)

if __name__=="__main__":
    y = dsp.TriangleSignal().make_wave().ys[:100]
    dft1 = DFT(y)
    dft2 = dspDFT(y)
    dft3 = npdft(y)
    t = np.linspace(0, len(y), len(y))
    #plt.plot(t, dft1)
    plt.plot(t, np.abs(dft2))
    #plt.plot(t, dft3)
    plt.show()

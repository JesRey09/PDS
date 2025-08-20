import numpy as np
import matplotlib.pyplot as plt

def mi_DFT(x):
    N = len(x)
    Xm = np.zeros(N, dtype=complex)
    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2 * np.pi * m * n) / N
            suma += x[n] * np.exp(-1j * arg)
        Xm[m] = suma
    return Xm

def exam_p2():
    fs = 256
    T = 6
    N = int(fs*T)
    n = np.arange(N)
    f1, f2 = 8, 20

    xn = np.sin(2*np.pi*f1*n/fs) + 0.5*np.sin(2*np.pi*f2*n/fs)
    Xm1 = mi_DFT(xn)

    tol = 1e-14
    Xm1.real[abs(Xm1.real) < tol] = 0
    Xm1.imag[abs(Xm1.imag) < tol] = 0

    m = np.arange(N)
    fan = m * fs / N

    plt.figure(1, figsize=(12,6))

    plt.subplot(2,1,1)
    plt.plot(n/fs, xn)
    plt.title("Señal discreta limpia en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")  
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm1[:N//2]))
    plt.title("Espectro (DFT) de la señal limpia")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()

    ruido = 0.7*np.sin(2*np.pi*10*n/fs)
    xn_ruidosa = xn + ruido
    Xm2 = mi_DFT(xn_ruidosa)

    Xm2.real[abs(Xm2.real) < tol] = 0
    Xm2.imag[abs(Xm2.imag) < tol] = 0

    plt.figure(2, figsize=(12,6))

    plt.subplot(2,1,1)
    plt.plot(n/fs, xn_ruidosa)
    plt.title("Señal discreta con ruido en el tiempo")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid()

    plt.subplot(2,1,2)
    plt.stem(fan[:N//2], np.abs(Xm2[:N//2]))
    plt.title("Espectro (DFT) de la señal con ruido")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("|X(f)|")
    plt.grid()

    plt.tight_layout()
    plt.show()

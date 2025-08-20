import numpy as np
import matplotlib.pyplot as plt

def mi_DFT(x):
    N = len(x)  # Cantidad de muestras
    Xm = np.zeros(N, dtype=complex)  # Contenedores de frecuencia
    
    # Fabricamos cada una de las componentes de frecuencia
    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2 * np.pi * m * n) / N
            suma += x[n] * np.exp(-1j * arg)
        Xm[m] = suma
    
    return Xm

# Señal continua
t = np.linspace(0, 0.001, 500)
xt = np.sin(2 * np.pi * 1000 * t) + 0.5 * np.sin(2 * np.pi * 2000 * t + 0.75 * np.pi)

# Discretización de la señal continua
fs = 8000.0  # Frecuencia de muestreo
n = np.arange(8)  # Índices de muestra
xn = np.sin(2 * np.pi * 1000 * n / fs) + 0.5 * np.sin(2 * np.pi * 2000 * n / fs + 0.75 * np.pi)

# Gráfica
plt.figure()
plt.plot(t, xt, 'm')
plt.stem(n / fs, xn)
plt.grid()

# Obtención de la transformada de Fourier discreta
Xm = mi_DFT(xn)

# Redondeamos a cero los valores diminutos
tol = 1e-14
Xm.real[abs(Xm.real) < tol] = 0
Xm.imag[abs(Xm.imag) < tol] = 0

# Índices de frecuencias discretas
N = len(Xm)
m = np.arange(N)

# Frecuencias de análisis
fan = m * fs / N

# Gráfica de la parte real, imaginaria, magnitud y fase de la DFT
plt.figure()

plt.subplot(2, 2, 1)
plt.stem(fan, Xm.real)
plt.grid()
plt.title('Parte real')

plt.subplot(2, 2, 2)
plt.stem(fan, Xm.imag)
plt.grid()
plt.title('Parte imaginaria')

plt.subplot(2, 2, 3)
plt.stem(fan, np.abs(Xm))
plt.grid()
plt.title('Magnitud')

plt.subplot(2, 2, 4)
plt.stem(fan, np.angle(Xm, deg=True))
plt.grid()
plt.title('Ángulo de fase')

# Cualquiera de las dos formas funciona
# Considerando la parte real y la parte imaginaria
Xtr = (2 / N) * (np.sin(2 * np.pi * 1000 * t) + np.sqrt(2) * np.cos(2 * np.pi * 2000 * t) - np.sqrt(2))

# Considerando la magnitud y la fase
Xxr = (2 / N) * (np.cos(2 * np.pi * 1000 * t - np.pi / 2) + 2 * np.cos(2 * np.pi * 2000 * t - np.pi / 4))

plt.figure()
plt.plot(t, Xtr, 'm')

plt.show()
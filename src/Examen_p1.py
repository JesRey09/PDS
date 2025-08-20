import numpy as np
import matplotlib.pyplot as plt

def exam_p1():

    fs = 100          # Frecuencia de muestreo en Hz
    T  = 1             # Duración de la señal en segundos
    N  = int(T*fs)     # Número de muestras
    t  = np.linspace(0, T, N, endpoint=False)  # Vector de tiempo


    x = (1 + 0.5 * np.cos(2 * np.pi * 0.5 * t)) * np.sin(2 * np.pi * 8 * t)

    X = np.fft.fft(x)
    X_mag = np.abs(X)/N           # Magnitud normalizada
    f = np.fft.fftfreq(N, 1/fs)  # Vector de frecuencias

    X_mag = X_mag[:N//2]
    f = f[:N//2]

    threshold = 0.1  # Umbral para detectar picos
    pico_indices = np.where(X_mag > threshold)[0]
    peak_freqs = f[pico_indices]
    peak_amps = X_mag[pico_indices]

    delta_f = fs / N
    print(f"Resolución en frecuencia Δf = {delta_f} Hz")

    print("Frecuencias de los picos:", peak_freqs)
    print("Amplitudes relativas:", peak_amps)

    plt.figure(figsize=(10,5))
    plt.stem(peak_freqs, peak_amps, 'r', basefmt=" ", label="Picos")
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Amplitud relativa")
    plt.title("Espectro de la señal")
    plt.legend()
    plt.grid()
    plt.show()
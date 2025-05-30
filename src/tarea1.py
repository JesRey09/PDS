import numpy as np
from src.utils.grapher import continuous_plotter, discrete_plotter


# 1. Señal senoidal continua
def continuous_sine():
    frequency = 2    #Seleccionamos la frecuencia en hz
    amplitude = 1    #Amplitud dada para la Señal senoidal continua
    number_of_points = 10000  #El numero de puntos dados para la señal discreta 
    time_initial = -1
    time_final = 5  
    time = np.linspace(time_initial, time_final, number_of_points) #Vector de tiempo continuo 
    x_t = amplitude * np.sin(2 * np.pi * frequency * time) # Señal senoidal sin(2πft)

    continuous_plotter(  #Se usa para graficar la senal de tiempo continuo que entra por el argumento 
        time, x_t,
        'Continuous Sine wave Signal', 'x₁(t) = sin(2π·f·t)',
        'Time [s]',  'Amplitude')


# 2. Señal senoidal discreta
def discrete_sine():
    frequency = 2 #Seleccionamos la frecuencia en hz 
    amplitude = 1  #Amplitud dada para la Señal senoidal discreta
    fs = 20   #Frecuencia de muestreo 20
    ts = 1 / fs #Peridodo de muestreo 
    samples = 100 #Indices de muestras de 0 a 99
    n = np.arange(samples) #señal muestreada
    x_n = amplitude * np.sin(2 * np.pi * frequency * n * ts)

    discrete_plotter(
        n, x_n,
        'Discrete Sine wave Signal', 'x₁[n] = sin(2π·f·n)',
        'Sample index [n]', 'Amplitude')


# 3. Señal exponencial continua x₂(t) = e^(–2t)·u(t)
def continuous_exponential():
    number_of_points = 1000
    time = np.linspace(-1, 5, number_of_points)
    u = np.heaviside(time, 1)  # Señal escalón unitario u(t)
    x_t = np.exp(-2 * time) * u  #Señal x(t) = e^(–2t) · u(t)

    continuous_plotter(
        time, x_t,
        'Continuous Exponential Signal', 'x₂(t) = e^(–2t)·u(t)',
        'Time [s]', 'Amplitude')


# 4. Señal exponencial discreta
def discrete_exponential():
    samples = 100
    ts = 0.05            #Periodo de muestreo 
    n = np.arange(-20, samples)   #Indices de muestra que van desde n = -20
    t = n * ts                    #Equivalencia para cada muestra 
    u = np.heaviside(t, 1)        #Escalon unitario 
    x_n = np.exp(-2 * t) * u      #Señal discreta exponencial

    discrete_plotter(
        n, x_n,
        'Discrete Exponential Signal', 'x₂[n] = e^(–2·n·Ts)·u[n]',
        'Sample index [n]', 'Amplitude')


# 5. Señal triangular continua
def continuous_triangle():
    from scipy import signal
    frequency = 2
    number_of_points = 1000 # Número de puntos para crear la señal suave la cual no tiene cambios bruscos 
    time = np.linspace(0, 2, number_of_points) # Vector de tiempo continuo de 0 a 2 segundos
    x_t = signal.sawtooth(2 * np.pi * frequency * time, 0.5)  # 0.5 → para al forma triangular simetrica 

    continuous_plotter(
        time, x_t,
        'Continuous Triangular Signal', 'x₃(t) = tri(t, f)',
        'Time [s]', 'Amplitude')


# 6. Señal triangular discreta
def discrete_triangle():
    from scipy import signal
    frequency = 2
    fs = 100
    ts = 1 / fs # Periodo de muestreo
    samples = 200   # Número total de muestras
    n = np.arange(samples)  # Vector de índices n = 0 a 199
    t = n * ts     # Vector de tiempos discreto para convertir n a tiempo real
    x_n = signal.sawtooth(2 * np.pi * frequency * t, 0.5)

    discrete_plotter(
        n, x_n,
        'Discrete Triangular Signal', 'x₃[n] = tri(n·Ts, f)',
        'Sample index [n]', 'Amplitude')


# 7. Señal cuadrada continua
def continuous_square():
    from scipy import signal
    frequency = 2
    number_of_points = 1000  # Cantidad de puntos en el vector tiempo
    time = np.linspace(0, 2, number_of_points) # Vector de tiempo de 0 a 2 segundos
    x_t = signal.square(2 * np.pi * frequency * time) # Para generar la señal cuadrada

    continuous_plotter(
        time, x_t,
        'Continuous Square Signal', 'x₄(t) = sq(t, f)',
        'Time [s]', 'Amplitude')


# 8. Señal cuadrada discreta
def discrete_square():
    from scipy import signal
    frequency = 2
    fs = 100
    ts = 1 / fs
    samples = 200
    n = np.arange(samples)
    t = n * ts   # Tiempo asociado a cada muestra
    x_n = signal.square(2 * np.pi * frequency * t)

    discrete_plotter(
        n, x_n,
        'Discrete Square Signal', 'x₄[n] = sq(n·Ts, f)',
        'Sample index [n]', 'Amplitude')
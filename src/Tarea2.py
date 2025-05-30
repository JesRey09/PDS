import numpy as np
from src.utils.grapher import continuous_plotter


def understanding_freq(des_freq):
    initial_time = 0  #seleccion del tiemo inicla de 0 segundos 
    end_time = 5     #Seleccion de tiempo final de 5 segundos 
    frequency = float(des_freq)   #Toma la frecuencia dada y la concierte a decimal 
    amplitude = 1             #Amplitud de la señal senoidal
    number_of_points = 1000  # Número de puntos del vector de tiempo
    time = np.linspace(initial_time, end_time, number_of_points)  #Vector de tiempo continuo de 0 a 5 con los 1000 puntos 
    xt = amplitude * np.sin(2 * np.pi * frequency * time) #Señal sinusoidal de la forma sin(2πft)
    continuous_plotter(time, xt,
    'Continuous Sine wave Signal', 'Sin wave Signal',
    'Time [s]', 'Amplitude')
import numpy as np
from src.utils.grapher import double_plotter, discrete_plotter

def compare_sine_signals(amplitude, frequency, phase):
    # Señal continua
    t = np.linspace(-1, 5, 1000)
    ref_cont = np.sin(2 * np.pi * 1 * t)
    mod_cont = amplitude * np.sin(2 * np.pi * frequency * t + phase)

    double_plotter(
        t, ref_cont, mod_cont,
        title="Comparación de señales senoidales (Tiempo continuo)",
        ref_label="Referencia: A=1, f=1Hz, ϕ=0",
        new_label=f"Modificada: A={amplitude}, f={frequency}Hz, ϕ={phase}",
        x_label="Tiempo (s)",
        y_label="Amplitud"
    )

    # Señal discreta
    Ts = 0.01
    n = np.arange(0, 600)
    t_discrete = n * Ts
    ref_disc = np.sin(2 * np.pi * 1 * t_discrete)
    mod_disc = amplitude * np.sin(2 * np.pi * frequency * t_discrete + phase)

    discrete_plotter(
        t_discrete, ref_disc,
        title="Señal discreta: Referencia",
        graph_label="Referencia",
        x_label="Tiempo (s)",
        y_label="Amplitud"
    )

    discrete_plotter(
        t_discrete, mod_disc,
        title="Señal discreta: Modificada",
        graph_label="Modificada",
        x_label="Tiempo (s)",
        y_label="Amplitud"
    )

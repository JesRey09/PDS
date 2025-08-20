import matplotlib.pyplot as plt
import numpy as np

def continuous_plotter(
    ind_var, dep_var,
    title: str = "", graph_label: str = "",
    x_label: str = "", y_label: str = ""
):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def discrete_plotter(
    ind_var, dep_var,
    title: str = "", graph_label: str = "",
    x_label: str = "", y_label: str = ""
):
    plt.stem(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def double_plotter(
    t, ref_signal, new_signal,
    title: str = "", ref_label: str = "Referencia", new_label: str = "Modificada",
    x_label: str = "Tiempo (s)", y_label: str = "Amplitud"
):
    plt.plot(t, ref_signal, 'r--', label=ref_label)
    plt.plot(t, new_signal, 'b-', label=new_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def dac_plotter(entradas_digitales, salida_analogica, bits):
    plt.figure(figsize=(8, 5))
    plt.step(entradas_digitales, salida_analogica, where='post', color='b', linewidth=2, label='Salida DAC')
    plt.scatter(entradas_digitales, salida_analogica, color='r')
    plt.title(f'Salida Analógica del DAC ({bits} bits)')
    plt.xlabel('Entrada Digital')
    plt.ylabel('Voltaje de Salida (V)')
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

def mi_DFT(x):
    N = len(x) #cantidad de muestras
    X = np.zeros( N, dtype=complex ) #Contenedores de frecuencia
    #Fabricamos cada una de las componentes de la frecuencia
    for m in range(N):
        suma = 0.0
        for n in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + x[n]*( np.cos(arg) - 1j*np.sin(arg) )

        X[m] = suma

    return X
        
def mi_IDFT(x):
    N = len(x) #cantidad de indices de frecuencia
    X = np.zeros( N, dtype=complex ) #Contenedores de amplitudes
    #Fabricamos cada una de las amplitudes de la señal
    for n in range(N):
        suma = 0.0
        for m in range(N):
            arg = (2*np.pi*m*n)/N
            suma = suma + X[m]*( np.cos(arg) + 1j*np.sin(arg) )

        x[n] = suma

    return x/N
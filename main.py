import sys
from src.Tarea1 import (
    continuous_sine, discrete_sine,
    continuous_exponential, discrete_exponential,
    continuous_triangle, discrete_triangle,
    continuous_square, discrete_square
)
from src.Tarea2 import understanding_freq


def main(options):
    if options[1] == "Tarea1":
        if len(options) < 3:
            print("Por favor especifica el tipo de señal: seno, exponencial, triangular, cuadrada")
            return

        signal_type = options[2].lower()

        if signal_type == "seno":
            continuous_sine()
            discrete_sine()
        elif signal_type == "exponencial":
            continuous_exponential()
            discrete_exponential()
        elif signal_type == "triangular":
            continuous_triangle()
            discrete_triangle()
        elif signal_type == "cuadrada":
            continuous_square()
            discrete_square()
        else:
            print("Tipo de señal no reconocido. Usa: seno, exponencial, triangular o cuadrada.")

    elif options[1] == "Tarea2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Por favor proporciona una frecuencia. Ejemplo: python main.py Tarea2 2")

    else:
        print("Opción no reconocida. Usa: Tarea1 o Tarea2")


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Por favor proporciona un argumento")
        print("Ejemplos:")
        print("  python main.py Tarea1 seno")
        print("  python main.py Tarea1 exponencial")
        print("  python main.py Tarea1 triangular")
        print("  python main.py Tarea1 cuadrada")
        print("  python main.py Tarea2 2")
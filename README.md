# 📊 Señales Continuas y Discretas con Python

Este proyecto genera y visualiza diferentes tipos de **señales matemáticas** (senoidales, exponenciales, triangulares y cuadradas) tanto en su forma **continua** como **discreta**. Está diseñado para propósitos educativos, especialmente para comprender el comportamiento de las señales en el dominio del tiempo.

---

## ⚙️ Sistema operativo y lenguaje

- 🖥️ **Sistema operativo:** Windows (compatible también con Linux/Mac)
- 🐍 **Lenguaje de programación:** Python 3.x

---

## 📁 Estructura del proyecto

```bash
proyecto_senales/
│
├── main.py                      # Código principal con las funciones de señales
├── freq_explorer.py            # Función interactiva para explorar la frecuencia de una senoidal
│
├── src/
│   └── utils/
│       └── grapher.py          # Contiene las funciones de graficación: continuous_plotter y discrete_plotter
│
├── requirements.txt            # Librerías necesarias para correr el proyecto
└── README.md                   # Este archivo



# Como ejecutar 
# 1. Clona o descarga el repositorio

git clone https://github.com/tuusuario/proyecto_senales.git
cd proyecto_senales

#2. Instala los requerimientos

pip install -r requirements.txt


# 3. Corre el código

python main.py
python freq_explorer.py


# Exámen: Análisis Espectral de Señales

## Objetivo
El objetivo es generar señales discretas y analizar su espectro en frecuencia utilizando Transformada Discreta de Fourier (DFT). 
Esto permite identificar los componentes de frecuencia dominantes, estudiar la resolución espectral de la señal y analizar cómo el ruido afecta al espectro.

## Dependencias
Este proyecto utiliza las siguientes librerías de Python:
- `numpy`
- `matplotlib`

Instalación recomendada:
```bash
pip install numpy matplotlib

##como ejecutar 
python Examen_P1.py  ## genera señal x(t) = (1 + 0.5 * cos(2π * 0.5 * t)) * sin(2π * 8 * t)
python Examen_P2.py  ## genera señales con y sin ruido xn = sin(2π*8*n/fs) + 0.5*sin(2π*20*n/fs)




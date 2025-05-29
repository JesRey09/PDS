import numpy as np 
import matplotlib.pyplot as plt
import control as ctl 

def singals_cont():
    """
        This fuction realice in a graphication    
    """

    # Determinate of time
    t = np.linspace(-1, 5, 1000)
    f = 2

    x_1 = np.sin(2*np.pi*f*t)
    #x_2 = (np.exp(-2*t)) * (1*t)
    #x_3 = np.tr(2*np.pi*f*t)
    x_4 = np.square(2*np.pi*f*t)

    plt.figure(1)

    plt.subplot(2,2,1)
    plt.plot(t, x_1, 'r')
    plt.grid()
    plt.title('Signal sin')

    plt.show()

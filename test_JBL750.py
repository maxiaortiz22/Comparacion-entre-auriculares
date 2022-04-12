from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import numpy as np
from SineSweep_promedio import sinesweep
from rta_frec import rta
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import ctypes

def A1():
    second = Toplevel()
    second.iconbitmap('logo.ico')
    second.title("Listo!")
    second.geometry("400x150")
    Label(second, text='Referencia grabada!').pack(pady=20)
    
    global left_F_1
    global right_F_1
    
    sinesweep2, filtro_inverso, T, Fs, P = sinesweep(20, 20000, 8, 44100, 1, 3)
    left_F_1, right_F_1 = rta(sinesweep2, filtro_inverso, T, Fs, P)

def A2():

    second = Toplevel()
    second.iconbitmap('logo.ico')
    second.title("Listo!")
    second.geometry("400x150")
    Label(second, text='Auricular cargado!').pack(pady=20)

    global left_F_2
    global right_F_2
    global Fs
    
    sinesweep2, filtro_inverso, T, Fs, P = sinesweep(20, 20000, 8, 44100, 1, 3)
    left_F_2, right_F_2 = rta(sinesweep2, filtro_inverso, T, Fs, P)

def calcular():
    global left_F_1
    global right_F_1
    global left_F_2
    global right_F_2
    global Fs

    rad = np.linspace(0, np.pi, int(len(left_F_1)/2))  # Vector de la fft en radianes
    f = rad/(np.pi/(Fs/2))  # Vecttor de la fft en Hz

    ftick = [20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000, 20000]
    labels = ['20', '31.5', '63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k', '20k']
    
    R_left = left_F_1[0:int(len(left_F_1)/2)] - left_F_2[0:int(len(left_F_2)/2)]
    R_right = right_F_1[0:int(len(right_F_1)/2)] - right_F_2[0:int(len(right_F_2)/2)]

    dif = [4.397552003,4.312593592,4.193818916,4.010830369,3.918242004,3.799707351,3.611496528,
    3.43761097,3.251825222,2.831863516,2.900432923,2.840178813,2.970520176,3.070702945,3.06011368,
    2.916266164,2.756218366,2.491591914,2.139783463,2.276498554,2.624326307,2.892120901,3.140312531,
    3.316502399,3.464754034,3.580872793,3.68918393,3.734420484,3.753366744,3.765464122,3.749312991,
    3.694073175,3.619915501,3.537587537,3.427514207,3.377571547,3.360642338,3.223078833,3.109863804,
    2.944869506,2.931625375,2.841712534,2.866311926,2.863961467,2.764679503,2.606078602,2.463568938,
    2.348494854,2.236612235,2.11452739,2.015833272,1.972123531,1.945074546,1.895652939,1.87487986,
    1.923182195,1.928181074,1.907401775,1.916575046,1.898209983,1.901963707,1.919948193,1.959719811,
    1.9938499,2.006850471,2.011270215,2.034432095,2.05314637,2.078141549,2.1584607,2.242304349,
    2.315727612,2.38996613,2.462531629,2.528382367,2.594435534,2.647399061,2.68981862,2.71899706,
    2.733937674,2.739650637,2.743457027,2.738429884,2.740415994,2.741196136,2.782760687,2.873273861,
    2.974496625,3.125103971,3.328930186,3.505540824,3.63012303,3.742292938,3.854827413,3.971595453,
    4.074068535,4.159974374,4.215845578,4.337346241,4.551026552,4.750081934,5.032781315,5.317555587,
    5.576469843,5.811451057,6.013677339,6.176157805,6.280936208,6.354048852,6.434991058,6.529327733,
    6.609802963,6.626502989,6.560496782,6.400028991,6.191877344,5.957954674,5.725653034,5.505356358,
    5.313714522,5.1470872,5.018742228,4.931789006,4.878846383,4.79860191,4.77897016,4.804529585,
    4.88398793,4.965250766,5.057337692,5.150341764,5.239949515,5.328167647,5.42180668,5.523813955,
    5.607329129,5.682625888,5.750768952,5.797208801,5.81212656,5.793390662,5.736230796,5.634281603,
    5.497394281,5.293687611,5.234795478,5.18547615,5.091020361,4.976031962,4.776284526,4.483114868,
    4.210712746,3.865340036,3.54683134,3.534543708,3.611325349,3.633084631,3.787085248,3.84971682,
    3.826805262,3.734516672,3.583540304,3.407046129,3.189848073,2.965674956,2.753396771,2.533142066,
    2.329897381,2.165096448,2.081429426,2.008452421,2.073295787,2.199136373,2.248965709,2.341543893,
    2.405593179,2.573176256,2.663849796,2.772906312,2.865907926,2.901657775,2.922272956,2.96596958,
    2.974702925,3.007300263,3.063520185,3.090798686,3.123202847,3.16195868,3.178434462,3.187621292,
    3.198692698,3.294582821,3.370270972,3.444127891,3.498937647,3.526503546,3.571349309,3.613622411,
    3.649747282,3.681802541,3.708591668,3.73613147,3.758822937,3.791624603,3.819468384,3.829918167,
    3.832368235,3.829462172,3.824156542,3.816664248,3.808780749,3.802001551,3.7863042,3.782498464,
    3.786466933,3.79466727,3.821118723,3.858977252,3.885025413,3.922804501,3.964383341,4.005678787,
    4.041812948,4.096459853,4.140337544,4.180087109,4.214093676,4.242569336,4.270105061,4.295953345,
    4.330605456,4.383784438,4.473894087,4.595179402,4.696373991,4.820899641,4.945673895,5.074720952,
    5.209885977,5.35021721,5.476624165,5.634976679,5.749745018,5.883421661,6.013738846,6.110514145,
    6.235073417,6.33992593,6.436016023,6.545561767,6.618472184,6.680804674,6.760712215,6.793367442,
    6.823694428]


    fig, axes = plt.subplots(2, 2)

    axes[0, 0].plot(f, left_F_1[0:int(len(left_F_1)/2)], label='Referencia')
    axes[0, 0].plot(f, left_F_1[0:int(len(left_F_1)/2)] + dif, 'r')
    axes[0, 0].plot(f, left_F_1[0:int(len(left_F_1)/2)] - dif, 'r')
    axes[0, 0].plot(f, left_F_2[0:int(len(left_F_2)/2)], label='Prueba')
    axes[0, 0].set_xlabel('Frecuencia [Hz]', fontsize=12, color='black')
    axes[0, 0].set_xscale('log')
    for axis in [axes[0, 0].xaxis]:
        axis.set_major_formatter(ScalarFormatter())
    axes[0, 0].set_ylabel('Amplitud izquierdo [dB]', fontsize=12, color='black')
    axes[0, 0].set_xlim([20, 20000])
    axes[0, 0].set_xticks(ftick)
    axes[0, 0].set_xticklabels(labels, rotation=90)
    axes[0, 0].legend()
    axes[0, 0].grid(True, which="both", ls="-")

    axes[0, 1].plot(f, right_F_1[0:int(len(right_F_1)/2)], label='Referencia')
    axes[0, 1].plot(f, right_F_1[0:int(len(right_F_1)/2)] + dif, 'r')
    axes[0, 1].plot(f, right_F_1[0:int(len(right_F_1)/2)] - dif, 'r')
    axes[0, 1].plot(f, right_F_2[0:int(len(right_F_2)/2)], label='Prueba')
    axes[0, 1].set_xlabel('Frecuencia [Hz]', fontsize=12, color='black')
    axes[0, 1].set_xscale('log')
    for axis in [axes[0, 1].xaxis]:
        axis.set_major_formatter(ScalarFormatter())
    axes[0, 1].set_ylabel('Amplitud derecho [dB]', fontsize=12, color='black')
    axes[0, 1].set_xlim([20, 20000])
    axes[0, 1].set_xticks(ftick)
    axes[0, 1].set_xticklabels(labels, rotation=90)
    axes[0, 1].legend()
    axes[0, 1].grid(True, which="both", ls="-")

    axes[1, 0].plot(f, R_left, label='Diferencia Izquierdo')
    axes[1, 0].set_xlabel('Frecuencia [Hz]', fontsize=12, color='black')
    axes[1, 0].set_xscale('log')
    for axis in [axes[1, 0].xaxis]:
        axis.set_major_formatter(ScalarFormatter())
    axes[1, 0].set_ylabel('Amplitud [dB]', fontsize=12, color='black')
    axes[1, 0].set_xlim([20, 20000])
    #axes[1, 0].set_ylim([-5, 5])
    axes[1, 0].set_xticks(ftick)
    axes[1, 0].set_xticklabels(labels, rotation=90)
    axes[1, 0].legend()
    axes[1, 0].grid(True, which="both", ls="-")

    axes[1, 1].plot(f, R_right, label='Diferencia Derecho')
    axes[1, 1].set_xlabel('Frecuencia [Hz]', fontsize=12, color='black')
    axes[1, 1].set_xscale('log')
    for axis in [axes[1, 1].xaxis]:
        axis.set_major_formatter(ScalarFormatter())
    axes[1, 1].set_ylabel('Amplitud [dB]', fontsize=12, color='black')
    axes[1, 1].set_xlim([20, 20000])
    axes[1, 1].set_xticks(ftick)
    axes[1, 1].set_xticklabels(labels, rotation=90)
    axes[1, 1].legend()
    axes[1, 1].grid(True, which="both", ls="-")

    plt.tight_layout()
    plt.show()


ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = Tk()
root.iconbitmap('logo.ico')
root.geometry("700x450")

root.title('Test de comparación entre auriculares - JBL 750')

frame = Frame(root, width=480, height=10)
frame.pack()

Label(root, text='').pack()

Button(root, text='\nAuricular de referencia\n', command=A1).pack()
Label(root, text='').pack()


Button(root, text='\nAuricular de prueba\n', command=A2).pack()


Label(root, text='').pack()
Label(root, text='').pack()

Button(root,text='Graficar', command=calcular).pack()
Label(root,text='').pack()


# Bucle de la aplicaciónon
root.mainloop()
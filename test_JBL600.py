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
    
    dif = [2.703200531, 2.505539539, 2.38852823, 2.412440043, 2.539834673, 2.588786964, 2.353998973, 
        2.340245828, 2.378513383, 2.48240106, 2.65160776, 2.853973994, 3.069871593, 3.119664265, 
        3.011310052, 3.137477268, 3.299808741, 3.392763441, 3.461462638, 3.338285646, 3.209746051, 
        2.961730042, 2.704154003, 2.440231996, 2.315981698, 2.254827911, 2.278716353, 2.311822887, 
        2.307333972, 2.273137309, 2.213779147, 2.148875155, 2.114506799, 2.108934381, 2.094744276, 
        2.093301451, 2.114421329, 2.121753153, 2.106544564, 2.104504181, 2.0918278, 2.059500285, 
        2.114751762, 2.092843844, 2.081949283, 2.049237133, 1.952194573, 1.916998474, 1.87309803, 
        1.875321509, 1.960024936, 2.03946313, 2.051728021, 2.036907356, 2.042140055, 2.051620526, 
        2.07617439, 2.177456473, 2.291026637, 2.273473389, 2.165755481, 2.103073826, 2.054749972, 
        2.025946951, 2.023329272, 2.031057989, 2.034534112, 2.03290429, 2.024060653, 2.0187685, 
        2.015332497, 2.01326947, 2.008334604, 2.005190443, 2.004920708, 2.001620984, 1.99809133, 
        1.991376453, 1.980068565, 1.971326025, 1.961477975, 1.949694097, 1.922249055, 1.894099148, 
        1.860116935, 1.831185578, 1.794919852, 1.806317999, 1.841016008, 1.881857243, 1.913161352, 
        1.993978516, 2.04890447, 2.08760882, 2.118554295, 2.154118315, 2.192258375, 2.243651566, 
        2.292485972, 2.339113107, 2.370189994, 2.421199474, 2.490656214, 2.572436895, 2.665170161, 
        2.751358723, 2.807962622, 2.833275005, 2.830482689, 2.817235046, 2.78848378, 2.755518286, 
        2.7171907, 2.686663426, 2.652583943, 2.637980714, 2.642542792, 2.645377005, 2.642049183, 
        2.639889352, 2.638675984, 2.63637619, 2.633602963, 2.618793899, 2.652447721, 2.648254256, 
        2.6402583, 2.650373794, 2.656203684, 2.655724854, 2.655699725, 2.645665981, 2.627669449, 
        2.606801429, 2.572370978, 2.524446451, 2.502158197, 2.476819157, 2.511352695, 2.5506445, 
        2.56687569, 2.596977035, 2.592817767, 2.553436785, 2.523699462, 2.481363818, 2.40924257, 
        2.588195791, 2.843440408, 3.087388398, 3.311227582, 3.510602181, 3.670211581, 3.791171485, 
        3.931545672, 4.226948043, 4.511167287, 4.812368653, 5.139800586, 5.455226324, 5.75270218, 
        6.019566245, 6.238257956, 6.400587447, 6.50048708, 6.747548015, 6.967480322, 6.888624385, 
        6.733854907, 6.668356064, 6.577237447, 6.423855048, 6.201149389, 5.902861869, 5.73268992, 
        5.540969958, 5.349602684, 5.14273704, 4.949154157, 4.763186764, 4.542627665, 4.336273083, 
        4.141385483, 4.049912561, 3.994141235, 3.87701018, 3.698988851, 3.535616692, 3.373930705, 
        3.207009824, 3.274638338, 3.418577895, 3.558243002, 3.684959191, 3.784037891, 3.842201922, 
        3.841581285, 3.772401613, 3.621888156, 3.432348468, 3.215684601, 3.031142244, 2.997255102, 
        3.027186101, 3.031153013, 2.997833029, 2.940207535, 2.859134485, 2.762778855, 2.725623121, 
        2.694194756, 2.647960565, 2.583151889, 2.508878769, 2.483281853, 2.466856156, 2.488322446, 
        2.53663346, 2.584859316, 2.687039553, 2.761253338, 2.81650629, 2.864566094, 2.894900109, 
        2.914036577, 2.919107444, 2.919208394, 2.903566082, 2.883239717, 2.859706461, 2.84223343, 
        2.819288797, 2.809957013, 2.854976821, 2.901427589, 2.961956259, 3.001439576, 3.034479166, 
        3.039948928, 3.046989782, 3.046307937, 3.037202023, 3.014638739, 2.986424213, 2.951864416, 
        2.920244333, 2.904284519, 2.882718179, 2.856657534, 2.828367003, 2.816292366, 2.798993959, 
        2.77967434, 2.759125003, 2.743704582, 2.744920003]


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

root.title('Test de comparación entre auriculares - JBL 600')

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
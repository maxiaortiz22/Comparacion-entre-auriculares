import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import sounddevice as sd
from scipy.fft import fft, ifft
from rta_frec import rta


def sinesweep(f_inf=20, f_sup=20000, T=5, Fs=44100, A=1, P=3):
    # Datos del sinesweep.
    f_inf = f_inf  # Frecuencia de inicio en Hz
    f_sup = f_sup  # Frecuencia de finalización en Hz
    T = T  # Duración en segundos
    Fs = Fs  # Frecuencia de sampleo
    A = A  # Amplitud (valor de 0 a 1)
    P = P  # Repetición, siempre mayor o igual a 1

    t = np.linspace(0, T, Fs*T)

    w1 = 2*np.pi*f_inf
    w2 = 2*np.pi*f_sup
    K = (T*w1)/(np.log(w2/w1))
    L = T/(np.log(w2/w1))

    theta = np.zeros(len(t))
    x_t = np.zeros(len(t))

    for i in range(len(t)):
        theta[i] = K*(np.exp(t[i]/L)-1)
        x_t[i] = np.sin(theta[i])  # sinesweep

    p = 1
    x_tp = []
    while p <= P:
        for i in range(len(x_t)):
            x_tp.append(x_t[i])  # concateno los sweeps
        p += 1

    norm = np.max(np.abs(x_tp))
    x_tNorm = np.zeros(len(x_tp))

    for i in range(len(x_tp)):
        x_tNorm[i] = x_tp[i]/norm  # sinesweep normalizado

    x_tNorm = np.multiply(x_tNorm, A)  # Determino su amplitud

    file_name = 'sinesweep_A{}_T{}_P{}.wav'.format(A, T, P)
    #sf.write(file_name, x_tNorm, Fs)

    # Modulacion
    w_t = (K/L)*np.exp(t/L)
    m_t = np.multiply(1/(2*np.pi*w_t), w1)

    m_tp = []
    p = 1
    while p <= P:
        for i in range(len(m_t)):
            m_tp.append(m_t[i])  # concateno los sweeps
        p += 1

    # Filtro Inverso
    x_t2 = np.flip(x_tp)
    k_t = np.multiply(m_tp, x_t2)  # Filtro inverso

    k_tNorm = np.zeros(len(k_t))
    norm = np.max(np.abs(k_t))

    for i in range(len(k_t)):
        k_tNorm[i] = k_t[i]/norm  # Filtro inverso normalizado

    k_tNorm = np.multiply(k_tNorm, A)  # Determino su amplitud
    file_name = 'inverso_A{}_T{}_P{}.wav'.format(A, T, P)
    #sf.write(file_name, k_tNorm, Fs)

    print("Se creó un sinesweep de {} a {} Hz, de {} segundos de duración, amplitud {} y promedio {}".format(f_inf, f_sup, T, A, P))

    return x_tNorm, k_tNorm, T, Fs, P





"""
sinesweep2, filtro_inverso, T, Fs, P = sinesweep(88, 11313, 1, 44100, 1, 3)

left_F, right_F = rta(sinesweep2, filtro_inverso, T, Fs, P)

rad = np.linspace(0, np.pi, int(len(left_F)/2))  # Vector de la fft en radianes
f = rad/(np.pi/(Fs/2))  # Vecttor de la fft en Hz

ftick = [20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000, 20000]
labels = ['20', '31.5', '63', '125', '250', '500', '1k', '2k', '4k', '8k', '16k', '20k']


fig, axes = plt.subplots(2, 1)

axes[0].plot(f, left_F[0:int(len(left_F)/2)], label='Izquierdo')
axes[0].set_xlabel('Frecuencia [Hz]', fontsize=15, color='black')
axes[0].set_xscale('log')
for axis in [axes[0].xaxis]:
    axis.set_major_formatter(ScalarFormatter())
axes[0].set_ylabel('Amplitud [dB]', fontsize=15, color='black')
axes[0].set_xlim([20, 20000])
axes[0].set_xticks(ftick)
axes[0].set_xticklabels(labels)
axes[0].legend()
axes[0].grid(True, which="both", ls="-")

axes[1].plot(f, right_F[0:int(len(right_F)/2)], label='Derecho')
axes[1].set_xlabel('Frecuencia [Hz]', fontsize=15, color='black')
axes[1].set_xscale('log')
for axis in [axes[1].xaxis]:
    axis.set_major_formatter(ScalarFormatter())
axes[1].set_ylabel('Amplitud [dB]', fontsize=15, color='black')
axes[1].set_xlim([20, 20000])
axes[1].set_xticks(ftick)
axes[1].set_xticklabels(labels)
axes[1].legend()
axes[1].grid(True, which="both", ls="-")


plt.tight_layout()
plt.show()



rad = np.linspace(0, np.pi, int(len(left_F)/2))  # Vector de la fft en radianes
f = rad/(np.pi/(Fs/2))  # Vecttor de la fft en Hz

ftick = [20, 31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000, 20000]

fig, ax = plt.subplots()
plt.plot(f, left_F[0:int(len(left_F)/2)], label='Izquierdo')
plt.suptitle('')
plt.xlabel('Frecuencia [Hz]', fontsize=15, color='black')
plt.xscale('log')
labels = [20, 31.5, 63, 125, 250, 500, '1k', '2k', '4k', '8k', '16k', '20k']
for axis in [ax.xaxis]:
    axis.set_major_formatter(ScalarFormatter())
plt.ylabel('Amplitud [dB]', fontsize=15, color='black')
plt.xlim([20, 20000])

plt.xticks(ftick, labels, fontsize=11)
plt.yticks(fontsize=11)
plt.legend()
plt.grid(True, which="both", ls="-")

plt.show()

fig, ax = plt.subplots()
plt.plot(f, right_F[0:int(len(right_F)/2)], 'g', label='Derecho')
plt.suptitle('')
plt.xlabel('Frecuencia [Hz]', fontsize=15, color='black')
plt.xscale('log')
labels = [20, 31.5, 63, 125, 250, 500, '1k', '2k', '4k', '8k', '16k', '20k']
for axis in [ax.xaxis]:
    axis.set_major_formatter(ScalarFormatter())
plt.ylabel('Amplitud [dB]', fontsize=15, color='black')
plt.xlim([20, 20000])

plt.xticks(ftick, labels, fontsize=11)
plt.yticks(fontsize=11)
plt.legend()
plt.grid(True, which="both", ls="-")

plt.show()


fig, (ax1, ax2) = plt.subplots(2)
ax1.semilogx(left_F[0:int(len(left_F)/2)])
ax2.semilogx(right_F[0:int(len(right_F)/2)])
plt.show()





time = np.linspace(0, T*P, T*Fs*P)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('LSS y filtro inverso', fontsize=20)
ax1.plot(time, sinesweep2)
ax1.set_ylabel('Amplitud [V]', fontsize=15)
ax2.plot(time, filtro_inverso)
ax2.set_xlabel('Tiempo [s]', fontsize=15)
ax2.set_ylabel('Amplitud [V]', fontsize=15)
plt.show()
"""
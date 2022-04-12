import numpy as np
import soundfile as sf
import sounddevice as sd
import time
from scipy.fft import fft, ifft

def rta(sinesweep2, filtro_inverso, T, Fs, P):
    print('Iniciando Sinesweep')
    sinesweep_play = np.zeros((len(sinesweep2), 2))

    for i in range(len(sinesweep2)):
        sinesweep_play[i, 0] = sinesweep2[i]
        sinesweep_play[i, 1] = sinesweep2[i]

    #print(sinesweep_play)
    myrecording = sd.playrec(sinesweep2, Fs, channels=2)
    time.sleep(T*P)

    sf.write('recording.wav', myrecording, Fs)

    left = np.zeros(len(myrecording[:, 0]))
    right = np.zeros(len(myrecording[:, 1]))

    for i in range(len(myrecording[:, 0])):
        left[i] = myrecording[i, 0]
        right[i] = myrecording[i, 1]


    filtro_inverso_f = fft(filtro_inverso)
    left_f = fft(left)
    right_f = fft(right)

    left_f = np.abs(left_f*filtro_inverso_f)
    right_f = np.abs(right_f*filtro_inverso_f)

    #left_f_aux = np.zeros(int(len(left_f)/P))
    #right_f_aux = np.zeros(int(len(right_f)/P))

    #for i in range(0, P):
        #for t in range(0,T*Fs+1):
            #left_f_aux += left_f[T*Fs*i:T*Fs*(i+1)]
            #right_f_aux += right_f[T*Fs*i:T*Fs*(i+1)]
            

    #left_f = left_f_aux/P
    #right_f = right_f_aux/P

    left_f = (left_f[0:T*Fs] + left_f[T*Fs:T*Fs*2] + left_f[T*Fs*2:T*Fs*3])/3
    right_f = (right_f[0:T*Fs] + right_f[T*Fs:T*Fs*2] + right_f[T*Fs*2:T*Fs*3])/3

    left_IR = ifft(left_f)
    right_IR = ifft(right_f)

    left_IR = left_IR[0:512] #Resolución hasta 86 Hz
    right_IR = right_IR[0:512] #Resolución hasta 86 Hz

    left_F = 20*np.log10(abs(fft(left_IR)) / (20*10**(-6)))
    right_F = 20*np.log10(abs(fft(right_IR)) / (20*10**(-6)))

    print('Fin Sinesweep')

    return left_F, right_F
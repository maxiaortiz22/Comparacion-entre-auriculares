import numpy as np
from SineSweep_promedio import sinesweep
from rta_frec import rta
import pandas as pd

#JBL600 sin ANC medidos a 80 de amplificación de la pc
#JBL600 con ANC medidos a 40 de amplificación de la pc
#JBL750 con ANC medidos a 40 de amplificación de la pc

sinesweep2, filtro_inverso, T, Fs, P = sinesweep(20, 20000, 8, 44100, 1, 3)
left, right = rta(sinesweep2, filtro_inverso, T, Fs, P)

left = left[0:int(len(left)/2)]
right = right[0:int(len(right)/2)]

data = {'Izquierdo': left, 'Derecho': right}

medicion = pd.DataFrame(data=data)

medicion.to_csv('JBL750 - 30.csv')
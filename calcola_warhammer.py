# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 10:34:50 2024

@author: lisaf
"""

import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt 


n_dadi = 6
colpire = 3
ferire = 3
danno = 3

start = 1 
stop = 6

n_tiri = 100000
hanno_ferito = []
hanno_colpito = []
tot_danno = []

for i in range(n_tiri):
    tiri_feriscono = 0
    tiri_colpiscono = 0
    for dado in range(n_dadi):
        tiro = randint(start, stop + 1)
        if tiro >= colpire:
            tiri_colpiscono += 1
            tiro = randint(start, stop + 1)
            if tiro >= ferire:
                tiri_feriscono += 1
                
    hanno_colpito.append(tiri_colpiscono)
    hanno_ferito.append(tiri_feriscono)
    tot_danno.append(tiri_feriscono * danno)

bins = np.arange(-0.5, n_dadi+1.5, 1)
fig = plt.figure()
ax = fig.add_subplot(121)
#plt.grid()
nc, binc, _ = ax.hist(hanno_colpito, bins = bins, color = 'grey', edgecolor = 'black', label = 'Colpiti', density = True, alpha = 0.7)
nf, binf, _ = ax.hist(hanno_ferito, bins = bins, alpha = 0.5, color = 'red', edgecolor = 'black', label = 'Feriti', density = True)
ax.legend()
ax.set_xlabel('Numero di Dadi')
ax.set_ylabel('Probabilità')
ax.set_axisbelow(True)
ax.grid()

print('Numero di dadi che colpiscono medi: ', np.mean(hanno_colpito))
print('Numero di dadi che feriscono medi: ', np.mean(hanno_ferito))


ax2 = fig.add_subplot(122)
bins = np.arange(min(tot_danno)-danno/2, max(tot_danno)+danno*1.5, danno)
nd, bind, _ = ax2.hist(tot_danno, bins = bins, color = 'grey', edgecolor = 'black', density = True, alpha = 0.7)

print('Danno medio: ', np.mean(tot_danno))

#ax2.legend()
ax2.set_xlabel('Q.tà di Danno')
ax2.set_ylabel('Probabilità')
ax2.set_axisbelow(True)
ax2.grid()
ax2.set_xticks((bins[:-1] + bins[1]))

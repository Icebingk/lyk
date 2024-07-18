import numpy as np
import matplotlib.pyplot as plt

t_list=np.arange(0,0.00001*4096,0.00001)

sample=np.sin(2*np.pi*1000*t_list)+np.sin(2*np.pi*2000*t_list)+np.sin(2*np.pi*3000*t_list)

out=np.fft.fft(sample)

plt.figure()
plt.plot(t_list,sample)

plt.figure()
plt.plot(t_list*10000,out.real)
plt.show()


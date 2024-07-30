import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, firwin,lfilter

t_list=np.arange(0,0.00001,1/(125000000))
t_list2=np.zeros(t_list.size*8)

for i in range(t_list.size):
    for j in range(8):
        t_list2[i*8+j]=t_list[i]+1/(125000000)/8*j

for i in range(20):
    print(t_list[i])

sample=(np.sin(2*np.pi*40000000*t_list)*(np.sin(2*np.pi*2000000*t_list+np.pi*1/3)))
sample3=(np.sin(2*np.pi*40000000*t_list2)*(np.sin(2*np.pi*2000000*t_list2+np.pi*1/3)))
sample2=np.zeros(sample.size*8)

for i in range(sample.size):
    for j in range(8):
        sample2[i*8+j]=sample[i]

fs = 125000000*8  # 采样频率
cutoff = 100000000  # 截止频率
numtaps = 29  # 滤波器阶数
b = firwin(numtaps, cutoff, fs=fs, pass_zero=True)

filtered_data = lfilter(b, 1.0, sample2)



out=np.fft.fft(sample)

plt.figure()
plt.plot(t_list2,filtered_data)

plt.figure()
plt.plot(t_list2,sample3)

plt.figure()
plt.plot(t_list*10000,out.real)
plt.show()


import bloodFunctions as b
import matplotlib.pyplot as plt

samples, duration, n = b.read("blood-data 2022-12-06 16:14:51 Sasha.txt")
t=[]
for i in range(n):
    t.append(i*duration/n)
#plt.plot(samples)
plt.plot(t[24000:60000], samples[24000:60000])
plt.show()
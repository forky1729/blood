import bloodFunctions as b
import time
import matplotlib.pyplot as plt

try:
     b.initSpiAdc()
     samples = []
    
     start = time.time()
     finish = start

     while (finish - start < 20):
          samples.append(b.getAdc())
          finish = time.time()
          print (b.getAdc())

     plt.plot(samples)
     plt.show()

     b.save(samples, start, finish)
finally:
     b.deinitSpiAdc()
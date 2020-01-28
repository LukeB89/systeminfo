'''
Created on 28 Jan 2017

@author: Luke
'''
import platform
import socket
import multiprocessing
import timeit
import math
from psutil import virtual_memory

 

def main():
    mem = virtual_memory()
    print("The Name of the computer is:", platform.node())
    print("The OS Name is:",platform.system())
    print("The OS Version is:", platform.version())
    print("The number of Cores is:",multiprocessing.cpu_count())
    print("The amount of memory in the computer is:",((mem.total/(1024**3))))
    print("The IP address is:",socket.gethostbyname(socket.gethostname()))
    t1 = timeit.default_timer()
    math.factorial(1000)
    t2 = timeit.default_timer()
    time = round((t2-t1)*1000000, 3)
    print("Time Taken: "+str(time)+" microseconds")
    

    return


if __name__ == '__main__':
    main()
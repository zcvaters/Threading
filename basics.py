import threading
import time

def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(0.85)
    print("now done")
'''
x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
time.sleep(1.2)
print("finally")
'''
ls = []

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.02)


def count3(n):
    for i in range(1, n*2):
        print(i)
        time.sleep(1)

#x = threading.Thread(target=count, args=(10,))
#x.start()

#y = threading.Thread(target=count2, args=(10,))
#y.start()

z = threading.Thread(target=count3, args=(10,))
z.start()

#x.join()

#y.join()

z.join()

#time.sleep(0.5)
#print(ls)


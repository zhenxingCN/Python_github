import threading
import time
import random
def worker(num):
    print('worker %s' % num)
    time.sleep(5)

def main():
    threads = []

    for i in range(5):
        t = threading.Thread(target=worker,args=(i,b))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    main()




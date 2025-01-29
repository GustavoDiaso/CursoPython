from threading import Thread, Lock
import time

my_lock = Lock()
def funcao(n):
    print("Estou sendo chamada pela thread", n)
    time.sleep(2)
    my_lock.acquire()
    print("Todas as execuções de 'funcao' foram bloqueadas nesse exato momento por mim, thread", n)
    for _ in range(1,4):
        print(_)
        time.sleep(2)

    print("Liberando a execução de 'função' por outras threads nesse exato momento...")
    time.sleep(5)
    my_lock.release()


thread1 = Thread(target=funcao, args=(1,))
thread2 = Thread(target=funcao, args=(2,))

thread1.start()
thread2.start()
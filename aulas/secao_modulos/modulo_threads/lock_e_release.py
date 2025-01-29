from threading import Lock, Thread
from time import sleep

class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """tenta comprar um ingresso"""

        """
        Lock.acquire() -> Interrompe todas as outras execuções desse metodo na fila de chamada
        ex:
        
        Considere que o método ingressos.comprar seja chamado primeiramente por thread1 e depois por thread2
        
        Como se tratam de threads, ambas as execuções acontecerão ao mesmo tempo, mas a execução do método comprar
        pela thread 1 foi feito primeiro
        
        como ingressos.comprar possui um Lock.aquire(), quando thread1 passar por esse comando, a execução do 
        método ingressos.comprar pela thread2 será pausada, até que o comando Lock.release() seja executado 
        pela thread1. 
        
        Isso impede que um mesmo método ou função seja executado ao mesmo tempo por 1 ou mais threads.
        """
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera as outras execuções do metodo, seguindo a ordem da fila de chamadas.
            self.lock.release()
            return

        sleep(3)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera as outras execuções do metodo, seguindo a ordem da fila de chamadas.
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        # Executa a thread e libera a execução do código
        t.start()

    print(ingressos.estoque)
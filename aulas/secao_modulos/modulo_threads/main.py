"""
O que são Threads?

Em Python, threads representam fluxos de execução concorrentes dentro de um mesmo processo. Imagine várias tarefas sendo
executadas simultaneamente, como se fossem mini-programas independentes dentro de um programa maior. Essa concorrência
permite que seu código aproveite melhor os recursos do processador, especialmente em sistemas multi-core, e pode
melhorar significativamente o desempenho em diversas aplicações.

Por que usar Threads em Python?

Concorrência: Permite executar múltiplas tarefas simultaneamente.

Responsividade: Mantém a interface do usuário responsiva, mesmo durante tarefas demoradas.

Eficiência: Pode melhorar o desempenho em tarefas I/O-bound (que envolvem muitas operações de entrada e saída),
operações de rede ou acesso a disco.
"""

from threading import Thread
import time

# Criando a minha Thread - forma 1 (Herança)
"""
class MyThread(Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        time.sleep(5)
        print("Execução simultânea finalizada")
    

my_thread = MyThread()
my_thread.start()

for _ in range(10):
    print(_)
    time.sleep(1)

"""

# Criando a minha Thread - forma 2

def my_function(nome:str):
    time.sleep(6)
    print(f'Olá, {nome}. (tarefa executada simultaneamente).')


my_thread = Thread(target=my_function, args=("Gustavo",))

# Executa a thread e libera a execução do código
my_thread.start()

# Retorna True se a thread especificada estiver sendo executada
while my_thread.is_alive():
    print('Executando thread...')
    time.sleep(2)
"""
generators em python são basicamente objetos iteráveis cujos valores só existem se forem acessados por um 
iterador.

A diferença de um generator para um iterável comum, é que os valores de um iterável comum são guardados na 
memória independentemente se serão acessados ou não.

Em suma, generators são iteráveis criados com o intuito de poupar a memória do computador. Seus valores 
são 'gerados' conforme são acessados via iterador (laço for, while, etc.)
"""

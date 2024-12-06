"""

No Python, arquivos .py são chamados de módulos. Cada módulo pode ser executado diretamente, como um programa em si, ou importado por outro módulo.

Quando um módulo é importado dentro de um código python, ele é executado por debaixo dos panos. Isso pode acarretar em diversos problemas.

Para que erros assim não ocorram, precisamos, de alguma maneira, identificar se nosso programa foi executado manualmente ou se essa execução deriva de uma 
importação. Para isso, temos uma variável nativa que pode nos auxiliar: a __name__, que nos indica o nome do contexto em que o módulo está rodando.

Resumindo, a variável __name__ representa o nome do módulo. Entretanto, quando o módulo é executado por si só como um programa, __name__ é definido
para '__main__', diferente de quando o módulo é importado, no qual o valor fica de fato igual ao nome do módulo.

se __name__ == '__main__', estamos executando nosso código diretamente.
se __name__ == 'nome do código', então o programa está sendo executado devido a um import
"""

def main():
    print("Hello World")


if __name__ == '__main__':
    main()



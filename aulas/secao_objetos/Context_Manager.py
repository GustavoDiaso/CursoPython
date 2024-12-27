"""
Gerenciadores de Contexto em Python

Gerenciadores de contexto em Python são mecanismos que simplificam a utilização e manipulação de recursos, garantindo
que eles sejam adquiridos e liberados de forma correta. Isso é especialmente útil ao lidar com recursos como arquivos,
conexões de banco de dados e outros objetos que requerem uma inicialização e finalização específicas.

Um gerenciador de contexto em Python funciona da seguinte forma:

"Abre" um recurso: Antes de usar um recurso (como um arquivo, uma conexão de banco de dados ou qualquer outro objeto
que precise ser gerenciado), o Python executa um código específico para prepará-lo.

"Usa" o recurso: Você realiza as operações desejadas com o recurso dentro de um bloco de código.

"Fecha" o recurso: Após o uso, ou se ocorrer algum erro, o Python executa outro código para liberar o recurso de
forma segura.

Ao centralizar o gerenciamento de recursos, você reduz o risco de esquecer de fechar um recurso, o que pode levar
a problemas de desempenho e até mesmo corromper dados.


Criando um Context Manager

A sintaxe with é usada para criar um contexto. Quando você entra em um bloco with, o metodo __enter__ do gerenciador de
contexto é chamado, e seu retorno é atribuído à variável local definida após o 'as'. Após isso, o bloco de código defi-
nido dentro da estrutura 'with as' é executado. Ao sair do bloco, seja por uma exceção ou pelo fluxo normal do
programa, o metodo __exit__ do gerenciador de contexto é chamado.

------------------------------------------------------------------------------------------------------------

O metodo __exit__ de um gerenciador de contexto em Python recebe três argumentos que fornecem informações sobre
qualquer exceção que possa ter ocorrido dentro do bloco with:

exc_type: O tipo da exceção que ocorreu. Se nenhuma exceção ocorreu, este valor será None.
exc_val: O valor da exceção, ou seja, a mensagem de erro. Novamente, será None se não houver exceção.
exc_tb: Um objeto traceback que contém informações sobre onde a exceção ocorreu. Também será None se não houver exceção.


O metodo __exit__ pode utilizar essas informações para:

Tratar a exceção: Você pode analisar o tipo e a mensagem da exceção para tomar decisões sobre como lidar com ela.
Por exemplo, você pode registrar a exceção em um log, tentar corrigir o problema ou até mesmo suprimir a exceção para
evitar que o programa seja interrompido.

Liberar recursos: Independentemente de ter ocorrido uma exceção ou não, o __exit__ é a oportunidade perfeita para
liberar os recursos adquiridos no __enter__, como fechar arquivos, conexões de banco de dados, etc. Isso garante que
os recursos sejam sempre liberados de forma correta, mesmo em caso de erros.

"""

class MyContextManager:
    """criando um novo gerenciador de contexto"""
    def __init__(self, host:str, database:str, table:str):
        self.host = host
        self.database = database
        self.table = table

    def __enter__(self):
        print("Método __enter__ sendo executado")
        print(f"Criando uma conexão com {self.host}/{self.database}/{self.table}")

        # Simulando o retorno da tabela especificada
        return ["Gustavo, 20, Adulto", "Isabela, 19, Adulta"]

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Método __exit__ sendo executado")
        print(f"Finalizando a conexão com {self.host}/{self.database}/{self.table}")



with MyContextManager('localhost', 'conhecidos', 'amigos') as tabela_amigos:
    print("\nBloco with sendo executado\n")
    for amigo in tabela_amigos:
        print(amigo)

    print('\n')





















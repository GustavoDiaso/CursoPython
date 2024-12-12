"""
Ambientes Virtuais em Python: Uma Explicação Completa

Ambientes virtuais em Python são  basicamente pastas isoladas dentro do seu sistema, onde você pode instalar 
e gerenciar versões específicas de pacotes Python para cada um dos seus projetos. Isso significa que você 
pode ter diferentes projetos, cada um com suas próprias dependências, sem que elas entrem em conflito 
umas com as outras.


Por que usar ambientes virtuais?

Isolamento de projetos: Cada projeto tem suas próprias necessidades e pode exigir versões diferentes de 
pacotes. Ambientes virtuais garantem que as dependências de um projeto não interfiram nas de outro.

Gerenciamento de versões: Você pode ter diferentes versões de um mesmo pacote instaladas em ambientes 
virtuais distintos, permitindo que você trabalhe em projetos que exigem versões específicas.

Facilidade de compartilhamento: Ao criar um ambiente virtual e instalar as dependências necessárias, 
você pode facilmente compartilhar seu projeto com outras pessoas, garantindo que ele funcione corretamente
em diferentes máquinas.

Organização: Mantém seus projetos mais organizados e evita conflitos de pacotes, especialmente em projetos 
maiores e mais complexos.

Ex 1:
Imagine que você esteja produzindo um código que necessita de uma biblioteca muito pesada para funcionar.
Instalando essa biblioteca dentro de um ambiente virtual, você garante que todos os programadores saibam
qual versão da biblioteca você utilizou, além de poupar espaço na pasta de bibliotecas global, uma vez que 
somente um programa a utilizará.

Ex 2:
Imagine que você esteja produzindo um código que precisa de uma versão mais antiga da biblioteca math, 
onde certa função ainda executava corretamente. Caso você instalasse a versão mais antiga na pasta global
de bibliotecas, TODOS os outros programas que você criou, que também utilizam math oriunda da pasta global, 
seriam afetados por tal mudança. Funções criadas na versão mais recente, agora substituída, parariam de 
funcionar completamente.

Pensando nisso, você criou e ativou um ambiente virtual, instalando a versão antiga de math dentro desse ambiente.
Dessa forma, a partir de agora, o 'import math' será feito a partir da biblioteca math presente no AMBIENTE 
VIRTUAL, não afetando qualquer outro programa. 

----------------------------------------------------------------------------------------

Como funcionam os ambientes virtuais?

Quando você cria um ambiente virtual, é como se estivesse criando uma nova instalação do Python, isolada 
da sua instalação principal. Isso significa que os pacotes instalados nesse ambiente não afetarão os 
outros projetos que você estiver trabalhando.


Por que é uma pasta "especial"?

A pasta do ambiente virtual não é uma simples pasta; ela está configurada para ser usada de maneira 
específica:

Quando você ativa um ambiente virtual, o Python "entende" que, tanto a versão do interpretador do python, 
quanto as bibliotecas que ele deve usar são aquelas instaladas no ambiente virtual, não mais aquelas 
presentes na pasta global de bibliotecas.

Quando você desativa, ele volta a usar o Python e as bibliotecas instaladas globalmente no sistema.

-------------------------------------------------
Criando um ambiente virtual:

O módulo venv do Python é a ferramenta padrão para criar ambientes virtuais. Para criar um ambiente 
virtual chamado meu_ambiente, você pode usar o seguinte comando no seu terminal:

python -m venv meu_ambiente

---------------------------------------------------------------------

Ativando Ambientes Virtuais no Windows

A ativação de um ambiente virtual serve exclusivamente para configurar o Python e o pip para usar as 
bibliotecas e o executável do ambiente virtual, em vez do ambiente global do sistema. 

Quando você ativa o ambiente virtual:

-> O interpretador Python usado será o que está dentro da pasta do ambiente.
-> Qualquer biblioteca que você instalar via pip vai para a pasta do ambiente virtual, sem afetar o sistema global.
-> O caminho padrão para python e pip é atualizado para o diretório do ambiente virtual.

Por outro lado, se você não ativar o ambiente e tentar usar python ou pip, o sistema continuará usando 
a instalação global, o que pode causar conflitos ou até erros.


Como ativar um ambiente virtual? (passo a passo)


1 - Abra o prompt de comando

2 - Navegue até o diretório do seu ambiente virtual: Utilize o comando cd para navegar até a pasta onde você 
criou o ambiente virtual. Por exemplo, se o seu ambiente se chama "meu_projeto" e está localizado na pasta 
"Projetos", você usaria:

cd Projetos\meu_projeto\Scripts

3 - Ative o ambiente virtual: Use o seguinte comando, substituindo "meu_projeto" pelo nome do seu ambiente:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\activate

"""

print("Olá")

# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example

import os
from dotenv import load_dotenv

# Instanciando nossas variáveis de ambiente
load_dotenv(r"C:\\Users\\Gustavo\\Documents\\GitHub\\CursoPython\\.env", override=True)


# Resgatando os valores das variaveis de ambiente criadas.
print(*os.environ, sep="\n")
print(os.getenv("USUARIO"))
print(os.getenv("SENHA"))

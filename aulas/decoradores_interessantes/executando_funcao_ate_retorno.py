from decorators.retry import retry

@retry(3, 2)
def conecta_ao_banco():
    raise Exception("Não conseguimos nos conectar ao banco de dados")


conecta_ao_banco()
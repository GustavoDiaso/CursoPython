# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

import datetime

def solucao(val_emprestimo: float, data_emprestimo: str, qtd_parcelas: int, dia_vencimento: int):

    # calculando data da primeira parcela
    data_emprestimo = datetime.datetime.strptime(data_emprestimo, '%d-%m-%Y')

    if data_emprestimo.day < dia_vencimento:
        data_primeira_parcela = data_emprestimo + datetime.timedelta(days=dia_vencimento-data_emprestimo.day)
    else:
        if data_emprestimo.month + 1 > 12:
            data_primeira_parcela = datetime.date(data_emprestimo.year+1, 1, dia_vencimento)
        else:
            data_primeira_parcela = datetime.date(data_emprestimo.year, data_emprestimo.month+1, dia_vencimento)



    parcela_atual = data_primeira_parcela
    val_das_parcelas = val_emprestimo / qtd_parcelas

    for num_parcela in range(1, qtd_parcelas+1):
        print(parcela_atual.strftime('%d-%m-%Y'), 'Valor: R$', round(val_das_parcelas, 2))

        # Calculando a quantidade de dias até o proximo vencimento (que é igual a quantidade de dias naquele mês)
        if parcela_atual.month + 1 > 12:
            ultimo_dia_do_mes = datetime.date(parcela_atual.year+1, 1, 1) - datetime.timedelta(days=1)
            dias_ate_prox_vencimento = ultimo_dia_do_mes.day
        else:
            ultimo_dia_do_mes = datetime.date(parcela_atual.year, parcela_atual.month+1, 1) - datetime.timedelta(days=1)
            dias_ate_prox_vencimento = ultimo_dia_do_mes.day


        # parcela_atual recebe a data do próximo vencimento
        parcela_atual = parcela_atual + datetime.timedelta(days=dias_ate_prox_vencimento)




solucao(200, '21-11-2025', 20, 20)
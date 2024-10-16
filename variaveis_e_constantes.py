"""
Em python, não existem constantes propriamente ditas, por isso, criou-se um consenso entre os programadores
de utilizar variáveis escritas em caps lock para referenciar dados que não deverão ser mudados ao longo 
do programa.

ex: 

VELOCIDADE_MAXIMA_PISTA = 80

"""

# criando um programa que verifica se o carro está na faixa do radar e aplica uma multa caso ele exceda 
# a velocidade máxima permitida na via


info_carro = {
    'posicao': 60,
    'velocidade_instantanea': 81
}

def aplica_multa(infoVeiculo):
    VELOCIDADE_MAXIMA_PERMITIDA = 80
    POSICAO_DO_RADAR = 60
    RAIO_DE_DETECCAO_RADAR = 4
    
    posicao_deteccao_minima = POSICAO_DO_RADAR - RAIO_DE_DETECCAO_RADAR
    posicao_deteccao_maxima = POSICAO_DO_RADAR + RAIO_DE_DETECCAO_RADAR

    if infoVeiculo['posicao'] in range(posicao_deteccao_minima, posicao_deteccao_maxima+1):
        if infoVeiculo['velocidade_instantanea'] > VELOCIDADE_MAXIMA_PERMITIDA:
            return "Você tomou multa"
            

    return "Você não tomou multa"

print(aplica_multa(info_carro))
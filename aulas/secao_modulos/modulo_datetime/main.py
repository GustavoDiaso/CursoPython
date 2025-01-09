import  datetime

data_aniversario = datetime.datetime(2004, 6, 19)

str_aniversario_irma = '2005-08-07 18:34:00'
date_format = '%Y-%m-%d %H:%M:%S'

data_aniversario_irma = datetime.datetime.strptime(str_aniversario_irma, date_format)


print(data_aniversario)
print(data_aniversario_irma)
print(datetime.date.today())

# Pegando a data atual
print(datetime.datetime.now())

# Comparando duas datas
data1 = datetime.datetime.strptime('2005-08-07 18:34:00', date_format)
data2 = datetime.datetime.strptime('2005-08-09 18:34:00', date_format)

print(data2 - data1)

# Criando um timedelta   (data_atual +- time_delta = nova_data)
delta = datetime.timedelta(days=10)
new_date = data2 + delta
# Convertendo data para string

str_new_date = new_date.strftime('%Y-%m-%d')
print(str_new_date)
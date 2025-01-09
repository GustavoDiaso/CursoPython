import  datetime

data_aniversario = datetime.datetime(2004, 6, 19)

str_aniversario_irma = '2005-08-07 18:34:00'
date_format = '%Y-%m-%d %H:%M:%S'

data_aniversario_irma = datetime.datetime.strptime(str_aniversario_irma, date_format)


print(data_aniversario)
print(data_aniversario_irma)
print(datetime.date.today())
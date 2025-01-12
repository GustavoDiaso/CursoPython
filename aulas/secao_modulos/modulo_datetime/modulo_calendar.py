# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

# print(calendar.calendar(2025))
# print("------------------------------------")
# print(calendar.month(2025, 6))


print(calendar.monthrange(2025, 6))
# (6, 30) = 6 - domingo  30 - ultimo dia do mês
print(list(calendar.day_name))

print(calendar.day_name[calendar.monthrange(2025, 6)[0]])

# descobrindo que dia da semana cai meu aniversário
dia_semana_aniversario = calendar.weekday(2025, 6, 19)
print(
    f"My birthday is on June 19th. It will be on {calendar.day_name[dia_semana_aniversario]} this year"
)

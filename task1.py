import sys

time, hourly_rate, prize = map(float, sys.argv[1:])
salary = time * hourly_rate + prize
print(f'Зарплата сотрудника при выработке = {time} час., ставке в час = {hourly_rate} руб., и премии = {prize} руб '
      f'будет равна {salary} руб.')

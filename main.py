#Ержанова Алмаш
#3лаб
#циклдарды қолданып жеке программа құру

'''total = 100
i = 0
while i < 5:
    n = int(input())
    total = total - n
    i = i + 1
print("Осталось", total)'''



'''пример на random'''
'''import random

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Выбор случайного города из списка - ", random.choice(city_list))'''



'''range() функциясын қолданып тізім жасау. 
range() функциясына әртүрлі типтегі мәндерді еңгізіп.
 әртүрлі мысалдар арқылы нәтижесін экранға шығару'''

from itertools import chain
merged = chain(range(5), range(10, 15))
for it in merged:
  print(it, end = ", ")


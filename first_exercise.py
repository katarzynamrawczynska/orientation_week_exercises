print('Hrwlsj')
my_variable = 7
my_variable2 = 'ala ma kota'
my_variable3 = None

my_variable = my_variable % 2
print('dsgdg ' + str(my_variable))
user_input = input('Wpisz swój wiek')

if int(user_input) >= 18:
    print('Jesteś pełnoletni')
elif int(user_input) >= 0:
    print('Nie jesteś pełnoletni')
else:
    print('Nie ma Cię!') 
for i in range(0,len(list1)):
    print(list1[i])

for el in list1:
    print(el)

list1 = [2, 5, 2, 8]
sum = 0

for el in list1:
    sum += el  # sum = sum + el
print(sum)


    # https://docs.python.org/3/library/math.html
    # https://docs.python.org/3/library/random.html

import math
def sum_numbers(a,b):
    a = a+2
    return a+b

l1 = sum_numbers(4,6)
l2 = sum_numbers(4,0)
l3 = l1 * l2
print(l3)
l1 = 5.7
print(math.floor(l1))



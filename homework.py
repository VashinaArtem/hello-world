#client = 'Petya'
#pet = 'cat'
#print(client)
#print('and')
#print(pet)

#r = 'Red'
#g = 'Green'
#b = 'Blue'
#print(r, g, b, r + g + b, b, g + b)

#first_animal = input('введите имя первого животного: ')
#second_animal = input('введите имя второго животного: ')
#print(first_animal, 'спит,', second_animal, 'идет')

#name = input('Введите имя: ')
#last_name = input('Введите фамилию: ')
#city = input('Введите город проживания: ')
#print('=========')
#print('Вас зовут', name, last_name)
#print('Выпроживаете в городе', city )

#first_name = input('Введите имя пользователя: ')
#greeting = 'Привет'
#print(greeting + ', ', first_name)
#print('К сожалению, у вас нет доступа к системе.')
#print('Пожалуйста, обратитесь к сис.админу.')

#departure_city = input('откуда вы вылетаете: ')
#arrival_city = input('куда вы собиратесь лететь: ')
#print(departure_city + '--' + arrival_city)

#login = input('Введите пользователя: ')
#file_name = input('Введите имя файла: ')
#print('Путь к файлу: ' + 'С:/' + login + '/docs/folder/' + file_name + '.txt')

#a = 'кек'
#b = 'кук'
#print(a, b)
#c = a
#a = b
#b = c 
#print(a, b)

#a = 8
#b = 10
#c = 12
#d = 18
#res = ((a**2 - 3)*b - (2**3))/(c-(2*d))
#print(res)

#first_num = int(input('за первый квартал: '))
#second_num = int(input('за второй квартал: '))
#third_num = int(input('за третий квартал: '))
#fourth_num = int(input('за четвертый квартал: '))
#first_sum = first_num + second_num
#second_sum = third_num + fourth_num
#res = first_sum/second_sum
#print(res)

#num = int(input('Введите число: '))
#print('После числа', num, 'идет число', num + 1)
#print('До числа', num, 'идет число', num-1)

#first_side = int(input('Введите длину первого катета: '))
#second_side = int(input('Введите длину второго катета: '))
#s = first_side*second_side/2
#print(s)

#time = int(input('Введите время: '))
#hours = time // 60
#print(time // 60, time % 60)

#first_num = int(input('Введите значение первого числа: '))
#second_num = int(input('Введите значение второго числа: '))
#print(first_num % 100 + second_num % 100)

#num = int(input('Введите четырехзначное число: '))
#thou = num//1000
#hun = (num - thou*1000)//100
#dec = (num - thou*1000 - hun*100)//10
#fig = num - thou*1000 - hun*100 - dec*10
#print(thou, hun, dec, fig )

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
print(a, b)
c = a - b
b += c
a -= c
print(a, b)


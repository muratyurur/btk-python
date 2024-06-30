# 1- "BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir carse oluşturunuz.
cars = ['BMW', 'Mercedes', 'Opel', 'Mazda']
print(cars)
# 2- Liste kaç elemanlıdır?
print(len(cars))
# 3- Listenin ilk ve son elemanı nedir?
print(f"Listenin ilk elemanı <{cars[0]}> ve son elemanı <{cars[-1]}>")
# 4- Mazda değerini Toyota ile değiştirin.
cars[-1] = 'Toyota'
print(cars)
# 5- Mercedes listenin bir elemanı mıdır?
print('Mercedes' in cars)
# 6- Listenin -2 indeksindeki değer nedir?
print(cars[-2])
# 7- Listenin ilk 3 elemanını alın.
print(cars[:3])
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
print(cars)
cars[-2:] = ['Toyota', 'Renault']
print(cars)
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
cars.append('Audi')
cars.append('Nissan')
print(cars)
# 10- Listenin son elemanını silin.
cars.pop()
print(cars)
# 11- Liste elemanlarını tersten yazdırın.
print(cars[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [70, 60, 70]]

students = [studentA, studentB, studentC]

print(students)

# 13- Liste elemanlarını ekrana yazdırınız.

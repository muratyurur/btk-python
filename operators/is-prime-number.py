number = int(input('Lütfen kontrol etmek istediğiniz sayıyı girin: '))
is_prime = True

if number == 1:
    print('1 asal sayı değildir.')
    is_prime = False

if number == 2:
    print('2 bir asal sayıdır.')

for num in range(2, number):
    if number % num == 0:
        is_prime = False
        break

if is_prime:
    print(f'{number} bir asal sayıdır.')
else:
    print(f'{number} bir asal sayı değildir.')

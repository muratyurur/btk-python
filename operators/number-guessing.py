import random

target = random.randint(1, 10)
lives = int(input('Kaç deneme hakkı olsun: '))
count = 0
score = 100
subtractor = score / lives

while lives > 0:
    lives -= 1
    count += 1
    guess = int(input('Tahmin: '))

    if target == guess:
        print(f'Tebrikler {count}. denemede buldunuz! Puanınız: {score}')
        break
    elif guess > target:
        print('Aşağı')
    else:
        print('Yukarı')

    score -= subtractor

if lives == 0:
    print(f'Ne yazık ki bulamadınız... Sayı: {target}')

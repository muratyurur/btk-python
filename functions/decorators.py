# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#
#     return wrapper
#
#
# @my_decorator
# def sayHello(name):
#     print("hello", name)
#
#
# sayHello("Murat")
import math
import time


def gecen_sure(func):
    def wrapper(*args, **kwargs):
        print("---------------------------------")
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(f"{func.__name__} fonksyionu {finish - start} saniye sürdü")

    return wrapper


@gecen_sure
def usAlma(a, b):
    print(math.pow(a, b))


@gecen_sure
def faktoriyel(num):
    print(math.factorial(num))


@gecen_sure
def toplama(a, b, c):
    print(a + b + c)


usAlma(2, 3)
faktoriyel(4)
toplama(125, 632, 456)

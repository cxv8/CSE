def challenge7(number):
    print(number+number*number+number**3)


challenge7(2)


def challenge1(first, last):
    print(last, first)


challenge1("Bob", "Dope")


def challenge4(number):
    if number >= 1:
        print("positive")
    if number <= -1:
        print("negative")
    if number == 0:
        print("zero")


challenge4(1)


def challenge3(number, number1):
    print(number*number1/2)


challenge3(6,2)


def challenge2(number):
    if number % 2 == 1:
        print("odd")
    if number % 2 == 0:
        print("even")


challenge2(22)


def challenge9(vowel):
    v = "aeiou"
    list1 = list(v)
    if vowel == list1[0]:
        print("vowel")
    elif vowel == list1[1]:
        print("vowel")
    elif vowel == list1[2]:
        print("vowel")
    elif vowel == list1[3]:
        print("vowel")
    elif vowel == list1[4]:
        print("vowel")
    elif vowel != list1[0] or list1[1] or list1[2] or list1[3] or list1[4]:
        print("not a vowel")


challenge9("e")


def challenge6(raduis):
    print(4/3*3.14*raduis**3)


challenge6(5)


def challenge5(raduis):
    print(3.14*raduis**2)


challenge5(3)


def challenge8(number):
    if number <= 1849:
        print("not enough")
    elif number >= 2151:
        print("too much")
    elif number <= 2150:
        print("enough")
    elif number >= 1850:
        print("enough")


challenge8(1859)


def challenge10(w):
    w = input("Enter a number ")
    if w.isdigit():
        print("digit")
    else:
        print("string")


challenge10(12)

import datetime
def challenge11(t):
    t.datetime.now().time()
    print(t.datetime.now().time())


challenge11(datetime)


def challenge12(a,b,c):
    for i in range(1,min(a,b)+1):
        if a%i==b%i==0:
            c = i
            print(c)


challenge12(22,44,0)
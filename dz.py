#-------------------1-------------------
'''
n = str(input())
def print_hello(name):
    print("Hello,", name + "!")

print_hello(n)
'''

#-------------------2-------------------
'''
num1 = int(input())
num2 = int(input())
if num1 < num2:
    num1, num2 = num2, num1

def gcd(n1, n2):
    if n1 == n2:
        return n1
    else:
        while (n1 > 0 and n2 > 0):
            if n1 > n2:
                n1 = n1 % n2
            else:
                n2 = n2 % n1
    return n1 + n2

print(gcd(num1, num2))
'''

#-------------------3-------------------
'''
n = int(input())
l = str(input())

month_name = {
              1: ["Январь", "January"],
              2: ["Февраль","February"],
              3: ["Март", "March"],
              4: ["Апрель","April"],
              5: ["Май","May"],
              6: ["Июнь","June"],
              7: ["Июль","July"],
              8: ["Август","August"],
              9: ["Сентябрь","September"],
              10: ["Октябрь","October"],
              11: ["Ноябрь","November"],
              12: ["Декабрь","December"]
}

la = {"ru" : 0, "en" : 1}
def month(n, lang):
    print(month_name[n][la[lang]])

month(n, l)
'''

#-------------------4-------------------
'''
words = []
def modern_print(word):
    if word not in words:
        words.append(word)
        print(word)
    else:
        return 0

modern_print("f")
modern_print("f")
'''
#-------------------5-------------------

n = input()
numbers = '0123456789'
n = ''.join(x for x in n if x in numbers)

def is_palindrome(num):
    if num == num[::-1]:
        return True
    return False
print(is_palindrome(n))
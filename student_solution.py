# В этом файле необходимо реализовать функции task1() ... task10()
# НИЧЕГО НЕ УДАЛЯТЬ
def task1():
   s = int(input())
   
   if s % 2 == 0:
       print("even")
   else:
       print("odd")

def task2():
    y = int(input())
    
    if y < 18:
        print("minor")
    elif y > 18 and y <= 64:
        print("adult")
    else:
        print("senior")

def task3():
    a = float(input())
    op = input()
    b = float(input())

    if op == '+':
        n = int(a+b)
        print(n)
    elif op == '-':
        n = int(a-b)
        print(n)
    if op == '*':
        n = int(a*b)
        print(n)
    elif op == '/':
        n = int(a/b)
        print(n)

def task4():
    num = int(input())
    num_2 = int(input())
    num_3 = int(input())
    
    if num > num_2:
        print(num)
        if num < num_2:
            print(num_2)

    if num_2 < num_3:
        print(num_3)
        if num_2 > num_3:
            print(num)

def task5():
    y = int(input())

   if y % 4 == 0 and y % 100 != 0:
       print("leap year")
   elif y % 400 == 0:
       print("leap year")
   else:
       ("not leap year")


def task6():
  temp = int(input())
    
  if temp < 0:
      print("freezing")
  elif temp <= 20:
      print("cool")
  elif temp <= 30:
      print("warm")
  else:
      print("hot")

def task7():
    grade = int(input())
    
    if grade == 90 or grade >= 100:
        print("A")
    elif grade == 75 or grade >= 89:
        print("B")
    elif grade == 60 or grade >= 74:
        print("C")
    elif grade == 40 or grade >= 59:
        print("D")
    else:
        print("F")

def task8():
    num = int(input())
    
    if num == 1:
        print("monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    else:
        print("Sunday")

def task9():
    a = int(input())
    b = int(input())
    c = int(input())

    if (a + b) > c and (b + c) > a and (a + c) > b:
        print("triangle exists")
    else:
        print("triangle does not exists")

def task10():
    

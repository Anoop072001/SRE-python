# x, y = int(input()), int(input())
# print(x**y)

# import math
# x = int(input())
# print(math.sqrt(x))

# x, y = int(input()), int(input())
# print(180-(x+y))


# a, b, c, d, e = int(input()), int(input()), int(
#     input()), int(input()), int(input())
# print("total:", a+b+c+d+e, "Avg.:", (a+b+c+d+e) /
#       5, "Percentage:", (a+b+c+d+e)/5, "%")


# P,T,R=int(input()),int(input()),int(input())
# print("simple interest:",(P*T*R)/100)


# p, t, r = int(input()), int(input()), float(input())
# print("Compound Interest:", (p*(1+r)**t)-p)

# n = int(input())
# sum = 0
# while(n > 0):
#     sum += n
#     n -= 1
# print(sum)

# a, b = int(input()), int(input())
# print((a+b)*(a-b))


# choice = int(input("Enter your choice\n1.even\n2.odd\n"))
# sum = 0
# no = 0
# n = int(input("How much numbers:"))
# if(choice == 1):
#     no += 2
#     for i in range(1, n+1):
#         sum += no
#         no += 2
# else:
#     no += 1
#     for i in range(1, n+1):
#         sum += no
#         no += 2
# print("sum:", sum)


# a, b = float(input()), float(input())
# print("Quotient:", a/b, "Remainder:", a % b)

# a = int(input())
# if(a > 0):
#     print("Positive")
# elif(a < 0):
#     print("Negative")
# else:
#     print("Zero")

# a = int(input())
# if(a % 2 == 0):
#     print("Even")
# else:
#     print("Odd")


# a = input()
# if(a == "a" or a == "A" or a == "e" or a == "E" or a == "i" or a == "I" or a == "o" or a == "O" or a == "u" or a == "U"):
#     print("Vowel")
# else:
#     print("Consonant")


# a = input()
# if(a.isdigit()):
#     print(a, "is a number")
# elif(a.isalpha()):
#     print(a, "is a alphabet")


# a, b = int(input()), int(input())
# if(a > b):
#     print(a, "is the largest")
# else:
#     print(b, "is the largest")

# a, b = int(input()), int(input())
# if(a < b):
#     print(a, "is the smallest")
# else:
#     print(b, "is the smallest")

# year = int(input())
# if(year % 100 == 0):
#     if(year % 400 == 0):
#         print(year, "is a leap year")
#     else:
#         print(year, "not a leap year")
# elif(year % 4 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "not a leap year")


# a, b, c = int(input()), int(input()), int(input())
# if(a > b and a > c):
#     print(a, "is the largest")
# elif(b > a and b > c):
#     print(b, "is the largest")
# elif(c > a and c > b):
#     print(c, "is the largest")


# a, b, c = int(input()), int(input()), int(input())
# if(a < b and a < c):
#     print(a, "is the smallest")
# elif(b < a and b < c):
#     print(b, "is the smallest")
# elif(c < a and c < b):
#     print(c, "is the smallest")


# a, b, c = int(input()), int(input()), int(input())
# if((a > b and a < c) or (a < b and a > c)):
#     print(a, "is the second largest and second smallest")
# elif((b > a and b < c) or (b < a and b > c)):
#     print(b, "is the second largest and second smallest")
# elif((c > a and c < b) or (c < a and c > b)):
#     print(c, "is the second largest and second smallest")


# n = int(input())
# order = len(str(n))
# sum = 0
# temp = n
# while(temp > 0):
#     digit = temp % 10
#     sum += digit**order
#     temp //= 10

# if(n == sum):
#     print("is armstrong")
# else:
#     print("is not armstrong")


# n = int(input())
# order = len(str(n))
# sum = 0
# temp = n
# while(temp > 0):
#     add = 1
#     digit = temp % 10
#     while(digit > 0):
#         add *= digit
#         digit -= 1
#     sum += add
#     temp //= 10
# if(sum == n):
#     print("is strong")
# else:
#     print("is not strong")


# n = int(input())
# sum = 0
# temp = n/2
# while(temp > 0):
#     if(n % temp == 0):
#         sum += temp
#     temp -= 1

# if(sum == n):
#     print("Perfect number")
# else:
#     print("Not perfect")


# n = int(input())
# if(n % 5 == 0):
#     print("Divisible")
# else:
#     print("Not divisible")


# a = input()
# if(a.isupper()):
#     print("Uppercase letter")
# else:
#     print("Lower case letter")

# n = int(input())
# if(n == 1):
#     print("Monday")
# elif(n == 2):
#     print("Tuesday")
# elif(n == 3):
#     print("Wednesday")
# elif(n == 4):
#     print("Thursday")
# elif(n == 5):
#     print("Friday")
# elif(n == 6):
#     print("Saturday")
# elif(n == 7):
#     print("Sunday")
# else:
#     print("wrong number")

# n = int(input())
# if(n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12):
#     print("31 days")
# elif(n == 2):
#     print("28 days")
# else:
#     print("30 days")


# 56
# p, ch, b, m, co = int(input()), int(input()), int(
#     input()), int(input()), int(input())
# percentage = ((p+ch+b+m+co)/500)*100
# if(percentage >= 90):
#     print("Grade A")
# elif(percentage >= 80):
#     print("Grade B")
# elif(percentage >= 70):
#     print("Grade C")
# elif(percentage >= 60):
#     print("Grade D")
# elif(percentage >= 40):
#     print("Grade E")
# else:
#     print("Grade F")


# 57
# bs = int(input())
# if(bs <= 10000):
#     hra = bs * 20/100
#     da = bs * 80/100
# elif(bs <= 20000):
#     hra = bs * 25/100
#     da = bs * 90/100
# else:
#     hra = bs * 30/100
#     da = bs * 95/100
# gs = bs+hra+da
# print("Gross Salary:", gs)


# 58
# e = int(input())
# if(e <= 50):
#     print("Rs.", e*0.50)
# elif(e <= 100):
#     print("Rs.", ((50)*0.50)+((e-50)*0.75))
# elif(e <= 250):
#     print("Rs.", (50*0.50)+(100*0.75)+((e-150)*1.20))
# elif(e > 250):
#     print((50*0.50)+(100*0.75)+(100*1.20)+((e-250)*1.50)+(e * 20/100))

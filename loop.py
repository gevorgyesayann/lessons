'''ciklnery linumen erku tesaki for and while'''
# fory ashxatuma voroshaki sahmanum, kara orinak bary bajani elementneri
# example
# for i in 'barev':
#     print(i)


# for cikli het kareli e gorcacel range()

# for i in range(10):
#     print(i)

# verjin tivy neraryal che


# while cikly aveli shat xndir grelu hamara
# sovorabar ogtagorcvuma 'while true' grelakargy

# import random as r
# user_point = 0
# pc_point = 0
# while True:
#     if user_point == 2 or pc_point == 2:
#         break
#     user = int(input('enter number (0,5)----'))
#     pc = r.randint(0,5)
#     if user == pc:
#         user_point += 1
#         print('user win', 'user points',user_point,   'pc points',pc_point)
#         continue
#     elif user != pc:
#         pc_point += 1
#         print('pc win', 'user points',user_point,   'pc points',pc_point)
#         continue


'''zip-y zugaher elementnery kapuma irar'''
# guyn = 'karmir', 'kapuyt'
# ararka = 'gndan', 'erkinq'
# for i,j in zip(guyn,ararka):
#     print(i,j)

# grel xndir while-ov, tpel 1-6 bnakan tvery

# i = 1
# while 1 < 6:
#     print(i)
#     i += 1

# for-i else haskacoxutyuny ogtagorcvume ayn jamanak erb uzumes yd=ndhanur ciklin hakadardz payman tas
# lezu = input('enter programming language----')
# text = 'python','django','js'
# for i in text:
#     if i == lezu:
#         print(i)
#         break
# else:
#     print('chka')
# ----------------------------------------------------



# Write a Python program to check if pc number is great than 10. random (1,20)
# when True break.

# import random as r

# while True:
#     pc = r.randint(1,20)
#     if pc > 10:
#         print(pc ,'tivy mec e tasic')
#         break
#     print(pc)

# ----------------------------------------------------


# Write a Python program to find the smallest number which are divisible by 12 and 15.

# x = 12
# y = 15
# for i in range(x, (x * y) + 1):
#     if i % x == 0 and i % y == 0:
#         print(i)
#         break

# ----------------------------------------------------


# 1-100 mijakayqum gtnel zuyg yev kent tveri qanaky

# zuyg_qanak = 0
# kent_qanak = 0
# for i in range(1,100 + 1):
#     if i % 2 == 0:
#         zuyg_qanak += 1
#     else:
#         kent_qanak += 1
# print(zuyg_qanak)
# print(kent_qanak)

# ----------------------------------------------------


# Write a Python program to get the Fibonacci series between 0 to 40:
# n1 = 0
# n2 = 1
# res = 0
# print(n1)
# print(n2)
# for i in range(0,40):
#     res = n1 + n2
#     n1 = n2
#     n2 = res
#     print(res)

# ----------------------------------------------------



# Write a Python program that accepts a string and calculate the number of digits and letters.

# text = 'python3.9'
# res = 0
# for i in text:
#     if i.isdigit():
#         res += int(i)
# print(res)
# ----------------------------------------------------


# Write a loop to find the factorial of any number. You have one input.

# tiv = int(input('enter number---'))
# res = 1
# for i in range(1,tiv + 1):
#     res *= i
# print(res)

# ----------------------------------------------------

# Write a Python program which have number (73421):
# You should calculate (7 + 3 + 4 ....):

# tver = (73421)
# res = 0
# for i in str(tver):
#     res += int(i)
# print(res)

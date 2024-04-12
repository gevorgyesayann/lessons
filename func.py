'''FUNCTION-- hnaravorutyuna talis konkret kody ashxatacnel konkret hatvacum'''

# def func():
#     return 'hello'
# print(func())

'''function-y yntunuma nayev argument'''

# def func(n):
#     return n ** 2
# print(func(6))


'''ete function-i mej piti for franq aveli lava grenq print() return - i texy'''

# def func(mylist):
#     for i in mylist:
#         print(i)
# func([1,2,3,4])

# def func(mylist):
#     for i in mylist:
#         print(i)
# x = [1,2,3,4]
# func(x)

# def func(a, b):
#     return a, b
# print(func(3,4))

# def child(child1,child2):
#     print('tariq1ov mec erexen ',child2)
# child (child1 = 'davit', child2 = 'gurgen')

'''function-y kara yntuni default parametr'''

# def my_func( country = 'armenia'):
#     print('i am from ',country)
# my_func()
# u inchqan avel parametr tanq hety ashxateluya
# my_func('sweden')

'''function-in karumenq nayev list tanq'''

# def func(food):
#     for i in food:
#         print(i)
# fruits = ['banan','xndzor','ananas']
# func(fruits)

# def func(x):
#     return 5 * x
# print(func(3))


'''pass ka eti ashxatacneluc error chi tali zut xndiry lucumes coment es anum pass y grumes u henc petqa ashxatacnes passy jnjumes'''

# def func():
#     pass


'''global-y function-i meji tvac arjeqnery ashxatucnma function-ic durs'''

# def func():
#     global x
#     x = 'fantastic'
# func()
# ----stex function-y prcnuma

# print(x)
# bayc stex ashxatuma

'''lambda-n funkciaya vory chuni voroshman tiruyt'''
'''lambda-n haytararum en popoxakanov'''

# lam = lambda x,y: x + y
# print(lam(2,3))

'''XNDIRNER'''

# 2. Write a python program to find max of two numbers.

# def func(x,y):
#     if x > y:
#         return x
#     elif y > x:
#         return y
# print(func(5,6))


# 3.Write a python program to sum all numbers.

# def func(mylist):
#     res = 0
#     for i in mylist:
#         res += i
#     print(res)
# func([1,2,3,4])


'''rekursiya'''
'''rekursian handisanuma anhrajesht bavarar payman xndri lucman hamar'''

# count = 0
# while True:
#     x = int(input('enter number---'))
#     if x == 4:
#         count += 1
#     if count == 3:
#         break
    # esi anhrajesht bavarar paymanna


'''factoriali xndir def-ov u rekursia'''
# def fact(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(5))



'''fibonaci xndir'''
# def func(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return func(n - 2) + func(n - 1)
# print(func(5))



'''DEKORATOR'''
'''dekoratory funkciaya vori mej grvuma funkcia vorpesi yndlayni mek ayl funkciya'''

# def good(n):
#     def decorator(x):
#         def gorcoxutyun(mylist):
#             return[x(i[0],i[1]) ** n for i in mylist]
#         return gorcoxutyun
#     return decorator

# @good(2)
# def func(a,b):
#     return a + b
# print(func([(1,2),(5,6)]))


'''dekoratornery linumen erku tesaki'''
'''vory vor uxaki dekoratora handisanum uxaki funkcia yndlaynelu hamar'''
'''yev vory parunakuma dekorator dekoratori funkcian yndlaynelu hamar'''



'''calculator xndir'''

# def cal(tiv1,tiv2,gorc):
#     if gorc == 'gumarel':
#         res = tiv1 + tiv2
#         return res
#     elif gorc == 'hanel':
#         res1 = tiv1 - tiv2
#         return res1
#     elif gorc == 'bajanel':
#         res2 = tiv1 / tiv2
#         return res2
#     elif gorc == 'bazmapatkel':
#         res3 = tiv1 * tiv2
#         return res3
# print(cal(1,2,'bazmapatkel'))


# 2.Write a python program to find max of two numbers.

# def func(a,b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
# print(func(8,4))
    

# 3. Write a python program to sum all numbers.

# def func(mylist):
#     sum = 0
#     for i in mylist:
#         sum += i
#     print(sum)
# mylist = [1,2,3,4,5]
# func(mylist)

# 5. Write a python program to sum all letter and number in your string.
# def func(text):
#     res = 0
#     res1 = 0
#     for i in text:
#         if i.isdigit():
#             res += int(i)
#         print(res)
# text = 'python3.9'
# func(text)



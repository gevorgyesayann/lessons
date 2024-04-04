'''TUPLE-y zangvac e vory karox e parunakel tarber tesaki elementner'''
# x = 12
# mytuple = (1,2.3,True,'barev',x)

'''TUPLE-y chpopoxvox data type e'''

'''TUPLE-i hishoxutyuny stugum en __sizeof__() konstruktori mijocov'''

# mytuple = (1,2,3,4,600000000000000000,1,2,3,4,5,56,6,77,8,8,9,9,90,0,0)
# print(mytuple.__sizeof__())


'''isinstance kochvuma yurahatuk irakan erb orinak petq e cuyc tal sahmanum arjeqi inch dzev yndunelu depqum inch klini'''

# num = [1,20,30,(20,30),50]
# c = 0
# for i in num:
#     if isinstance(i, tuple):
#         break
#     c += 1
# print(c)


'''reversed hramanov tuply shrjum enq'''

# mytuple = (1,2,3,4,5)
# x = reversed(mytuple)
# print(tuple(x))


# 1. Write a Python program to count the elements in a list until an element is a tuple.

# mytuple = (1,2,3,[5,4,3],7)
# res = 0
# for i in mytuple:
#     if isinstance(i, list):
#         break
#     res += 1
# print(res)


# 2. Write a Python program to reverse a tuple.

# mytuple = (1,2,3,4,5)
# x = reversed(mytuple)
# print(tuple(x))


# 5. Write a Python program which calculate the count of item in
# tuple for example: my_tuple = (1,12,15) output:28.

# tuple = (1,12,15)
# res = 0
# for i in tuple:
#     res += i
# print(res)


# 4. Write a Python program to convert a tuple to a string.

# tuple = (1,2,3,4)
# res = ''
# for i in tuple:
#     res += str(i)
# print(res)


# 6. Write a Python program to find name in tuple.

# name = input('enter name---')
# mytuple = ('Gevorg','Narek','Hovsep')
# for i in mytuple:
#     if i == name:
#         print('ka')
#     else:
#         print('chka')

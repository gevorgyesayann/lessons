'''PASSWORD-i xndir'''
# while True:
#     char_count = 0
#     number_count = 0
#     char_list = ['!','@','#','$','%']
#     password = input('enter password--')
#     if len(password) < 8:
#         print('paswordy petq e parunaki 8 nishic voch pakas')
#         continue
#     else:
#         for i in password:
#             if i in char_list:
#                 char_count += 1
#             if i.isdigit():
#                 number_count += 1
#             if number_count >= 1 and char_count >= 1:
#                 print('your password is strong')
#                 break
#         else:
#             print('passwordy petq e parunaki tiv yev element')
#             continue
#         break


'''link-i xndir'''
# Create python program where you want to find id in link if link have id print id.
# Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
# Sample Output: RWW2aUSwvU

# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# print(link[link.index('=') + 1:])


'''poligrom xndir'''
# Create python program where you want to check if input word is palindrome or no .if yes print Open otherwise Trash
# Sample Input: RACECAR
# Sample Output: Open

# bar = input('enter word---')
# if bar == bar[:: -1]:
#     print('open')
# else:
#     print('trash')

'''string-y listi convert anel'''
# Create python program to convert string to a list.
# string1 = 'millioner'
# string1 = string1.split(' ')
# print(string1)

# Create python program which will show all even numbers in your
# string. Note: you have input where have 5 numbers:
# Sample Input: 12 21 15 19 8
# Sample Output: 128

# tver = input('enter numbers---')
# tver = tver.split(' ')
# print(tver)
# for i in tver:
#     if int(i) % 2 == 0 and i != 0:
#         print(i)

# Write a Python program to select the odd items of a list. And delete even items.
# list1 = [1,2,3,4,5,6]
# for i in list1:
#     if i % 2 == 0:
#         list1.remove(i)
# print(list1)
# ----------------------------------------------------------------------

'''DICTIONARIES'''
'''dict-y ogtagorcum en real npatakneri hamar'''
'''grum en dzevavor pakagcerov {}'''
# mydict = {}

'''dicty uni 2 arjeq key and value'''
# dict_name = {
#     1:'Armen',
#     2:'Tigran',
#     3:'Arthur'
# }
# print(dict_name)
# karelia tpel miayn vlaue-nery
# mydict = {
#     1:'narek'
# }
# print(mydict.values())
# nayev miayn key-ery
# mydict = {
#     2:'gagik'
# }
# print(mydict.keys())

# dict-i meji elementi value-n poxumen key-y nshelov
# nory avelacnum enq nor key anun talov

# mydict = {
#     'name': 'Dinar'
# }
# mydict['name'] = 'Dinara'
# mydict['surname'] = 'Fayzulayeva'
# print(mydict)

'''DICT-i methodner'''

# popitem() methody erjin elementy jnjuma
# mydict = {
#     1: 'name1',
#     2:'name2',
#     3:'name3'
# }
# mydict.popitem()
# print(mydict)

# dict0i mejic element jnjel 
# thisdict = {
#     1:'Ahmad',
#     2:'Harini',
# }
# del thisdict[1]
# print(thisdict)

# clear()--- maqruma dict-y
# mydict = {
#     1:2,
#     3:4
# }
# mydict.clear()
# print(mydict)

# cop()-- nuyn dictna talis
# mydict = {
#     1:1,
#     2:3
# }
# res = mydict.copy()
# print(res)

# get()-- veradarcnuma keyin hamapatasxan value
# mydict = {
#     1:1,
#     2:3
# }
# print(mydict.get(2))

# pop()-- jnjuma elementy, printi mej tpelu depqum cucya tali jnjac elementy
# mydict = {
#     1:1,
#     2:3
# }
# print(mydict.pop(2))
# print(mydict)

# popitem()--- jnjumer verjin elementy
# mydict = {
#     1:1,
#     2:3
# }
# mydict.popitem()
# print(mydict)

# setdefault()--y erku list kpcnuma irar u sarquma dict
# tox = '1j2k3h4m5a7'
# list1 = []
# list2 = []
# dict1 = {}
# for i in tox:
#     if i.isdigit():
#         list1.append(i)
#     else:
#         list2.append(i)
# for n,m in zip(list1,list2):
#     dict1.setdefault(n,m)
# print(dict1)


# update()---y dicty avelacnuma dictin
# dict1 = {
#     1:1,
#     2:2
# }
# dict2 = {
#     3:3,
#     4:4
# }
# dict1.update(dict2)
# print(dict1)

'''XNDIRNER'''

# 1. Write a Python program to sort a dictionary by value.
# mydict = {
#     1:2,
#     2:1,
# }
# mydict1 = sorted(mydict.values())
# print(mydict1)

# 2. Write a Python program to add a key to a dictionary.
# mydict = {
#     1:1,
#     2:2,
# }
# mydict[3] = 3
# print(mydict)

# 3. Write a Python program to check whether a given key already exists in a dictionary.
# x = input('enter key---')
# mydict = {
#     '1':1,
#     '2':2,
#     '3':3,
#     '4':4
# }
# for i in mydict:
#     if x in i:
#         print('ka')


# 4. Write a Python program to merge two Python dictionaries.
# dict1 = {'a': 50, 'b': 700}*
# dict2 = {'c': 400, 'd': 600}
# output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}

# dict1 = {
#     'a':50,
#     'b':700
# }
# dict2 = {
#     'c':400,
#     'd':600
# }
# dict1.update(dict2)
# print(dict1)

# 5. Write a Python program to multiply all the values in a dictionary.
# For example:
# mydict = {'a':1, 'b':2, 'c': 12} output: 24
# mydict = {
#     'a':1,
#     'b':2,
#     'c':12
# }
# res = 1
# for i in mydict.values():
#     res *= i
# print(res)

# 6. Create a Python program to find the highest 3 values in a dictionary.
# {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# output: {'F': 69, 'A': 67, 'D': 56}
# mydict = {
#     'D': 56,
#     'E': 12, 
#     'F': 69, 
#     'C': 45, 
#     'B': 23, 
#     'A': 67
#     }
# mydict1 = sorted(mydict, key = mydict.get, reverse=True )[:3]
# mydict2 = sorted(mydict.values(), reverse = True)[:3]
# mydict3 = {}
# for i,j in zip(mydict1,mydict2):
#     mydict3.setdefault(i,j)
# print(mydict3)


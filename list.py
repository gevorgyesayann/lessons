''' LIST-y popoxvox data type-a'''
'''LIST-i mej hnaravora pahel tarber tesaki elementner, bayc list-y uni mi sharq methodner voronq ayd depqum chen ashxati'''
'''dra hamar sovorabar list-i mej pahum en miatesak elementner'''


# tvery sortavoruma ajman karqov
# list1 = [1,6,5,4,3,2]
# list1.sort()
# print(list1)

# tarery sortavoruma aybenakan kargov
# list_tarer = ['ab','ba','dfa','ggg','cfv','23245676']
# list_tarer.sort()
# print(list_tarer)
# ete listi mej ka string vory parunakuma tiv demic et stringy sortavorman jamanak galisa araj

# kareli e sortavorel yst erkarutyan

# list_tarer = ['ab','ba','dfa','ggg','cfv','23245676']
# list_tarer.sort(key=len)
# print(list_tarer)
# ---------------------------------------------------------

'''LIST-I HRAMANNER'''

# append() hramany avelacnuma listin element
# list1 = [1,2,3,4]
# list1.append(5)
# print(list1)
# cankalia avelacnel nuyn tipi elementner

'''indexneri vra for fral'''
# list1 = ['a','b','g','d','j']
# for i in range(0, len(list1)):
#     print(i)


# arajin indexi taki elementy poxel 
# list1 = [1,23,4,5,6]
# list1[1] = 8
# print(list1)

# insert()--- listi konkret indexum avelacnuma element
# list1 = [1,2,3,45,6]
# list1.insert(1, 5)
# print(list1)


# remove()--- list-i konkret elementy nshelov jnjuma
# list1 = [4,5,8,9,2,3,4,1]
# list1.remove(8)
# print(list1)


# # del--- jnjuma yst index-i
# list1 = [1,2,3,4,5]
# del list1[1]
# print(list1)

# pop()-- jnjuma verjin elementy
# list1 = [1,2,3,5,6,8]
# list1.pop()
# print(list1)
# ete nshel indexy edpesel kashxati
# list1 = [1,6,7,85,3]
# list1.pop(1)
# print(list1)

# clear()-- maqruma listy
# list1 = [1,2,4,3,6,0]
# list1.clear()
# print(list1)

# extend()--- listy kpcnuma listin
# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)

# sort()--- sortavora listy
# list1 = [4,3,6,8,9,1]
# list1.sort()
# print(list1)

# reverse()--- shrjuma listy
# list1 = [1,2,3,4,5]
# list1.reverse()
# print(list1)

# copy()--- nuynakerp lista stexcum 
# list1 = [1,2,3,45]
# list1.copy()
# print(list1)

# count()-- hashvuma listi mej nshac elementic qani hat la
# list1 = [1,2,3,5,5,5]
# x = list1.count(5)
# print(x)

# index()---- cuyca talis trvac elementy vor indexuma gtnvum listi mej
# list1 = [1,2,3,4,5]
# x = list1.index(5)
# print(x)
# -----------------------------------------------


''' XNDIRNER'''

# 1. hashvel listi meji tveri gumary
# list1 = [1,2,3,4,5]
# res = 0
# for i in list1:
#     res += i
# print(res)

# 2. Wiite a Python piogiam to multiplies all the items in a list.
# list1 = [4,7,8,9,1]
# res = 1
# for i in list1:
#     res *= i
# print(res)

# 3. Write a Python program to get the largest text from a list.
# list1 = ['barev','alo','hajox','ha']
# arajin tarberak
# print(max(list1))
# erkrord tarberak
# list1.sort(key = len)
# print(list1[-1])


# 4. Write a Python program that have two lists and returns True if they have at least one common member.
# list1 = [1,2,3,4]
# list2 = [4,5,6,7]
# for i in list1:
#     for j in list2:
#         if i == j:
#             print(True)


# Create new list which have data notebooks and you want check if the data have Mac?
# x = input('entern notebook type---')
# list1 = ['hp','lenovo','acer','mac']
# if x in list1:
#     print(True)

# Create a python program which delete all duplicate items in list.
# list1 = [1,2,3,4,1]
# for i in list1:
#     if list1.count(i) > 1:
#         list1.remove(i)
# print(list1)

# list1 = [1,2,3,4,56,1]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# Write a Python program to select the odd items of a list. And delete even items.
# list1 = [1,2,3,4,56,7]
# for i in list1:
#     if i % 2 == 0:
#         list1.remove(i)
# print(list1)
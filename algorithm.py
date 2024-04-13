'''es algoritmnery ashxatanqy tetevacnelu hamara'''
'''orinak meky index()---y eti algoritma'''

# list1 = [1,2,3,4]
# x = int(input('enter number---'))
# if x in list1:
#     print(list1.index(x))
# else:
#     print('chka')

'''hima es index()--i logikan grenq linear search-ov'''
'''linear search'''

# list1 = [1,2,3,4]
# x = int(input('enter number---'))
# for i in range(0,len(list1)):
#     if list1[i] == x:
#         print(i)
# ---------------------------------------------

'''binary search'''
# def test(list1,x,start,stop):
#     mid = (start + stop) // 2
#     if x == list1[mid]:
#         return mid
#     elif x < list1[mid]:
#         return test(list1,x,start, mid - 1)
#     else:
#         return test(list1,x,mid - 1,stop)
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# x = int(input('enter number---'))
# start = 0
# stop = len(list1)
# print(test(list1, x, start, stop ))
# -----------------------------------------------

'''buble search'''

# mylist = [10, 75, 43, 15, 25, -4, 27]
# for i in range(0, len(mylist) - 1):
#     for j in range(0, len(mylist) - i - 1):
#         if mylist[j] > mylist[j + 1]:
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

# print(mylist)


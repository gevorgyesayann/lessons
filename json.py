# import json 
# user = {'es qez sirumem':'Dinara'}

# with open('dict.json', 'w') as file:
#     json.dump( user , file)
    

# '''terminalum tpelu hamar load enq anum json file-y'''


# f = open('dict.json')
# res  = json.load(f)
# # print(res)
# # for i in res:
# for i in res.values():
#     print(i)



# import json 


# user1 = {
#     'name':'Gevorg',
#     'year':2007,
#     'profesion':'programmer'
#     }



# user2 = {
#     'name':'Dinara',
#     'year':2008,
#     'profesion':'dancer'
#     }


# users = [user1,user2]

# with open('about_users.json', 'w') as file:
#     json.dump(users, file)

# f =  open('about_users.json')
# res =  json.load(f)
# for i in res:
#     print(i)



# import json


# user1 = {
#     'name':'Gevorg',
#     'year':2007,
#     'profession':'programmer'
# }

# with open('aboutme.json', 'w') as file:
#     json.dump(user1,file)

# f  = open('aboutme.json')
# res = json.load(f)
# x = input('enter name--')
# if x in res.values():
#     print(True)
# else:
#     print(False)

# import json


# list = [1,2,3]
# list1 = ['ani','jessy','ben']
# dict1 = {}
# for i,j in zip(list,list1):
#     dict1.setdefault(i,j)


# with open('dict1.json', 'w') as file:
#     json.dump(dict1, file)
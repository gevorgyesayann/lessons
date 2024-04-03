# 1. Take two int values from user and print greatest among them.


# x = int(input('enter  first number--'))
# y = int(input('enter second number--'))
# if x > y:
#     print('arajiny meca')
# elif y > x:
#     print('erkrordy meca')
# else:
#     print('havasar en')

# --------------------------------------------------

#2. Take input of age of 3 people by user and determine oldest and youngest among them.

# user1 = int(input('arajin mardu tariqy----'))
# user2 = int(input('erkrord mardu tariqy----'))
# user3 = int(input('errord mardu tariqy----'))

# if user1 > user2 and user2 > user3:
#     print('amenamecy', user1)
#     print('amenapoqry',user3)
# elif user1 > user3 and user3 > user2:
#     print('amenamecy', user1)
#     print('amenapoqry',user2)
# elif user2 > user1 and user1 > user3:
#     print('amenamecy', user2)
#     print('amenapoqry',user3)
# elif user2 > user3 and user3 > user1:
#     print('amenamecy', user2)
#     print('amenapoqry',user1)
# elif user3 > user1 and user1 > user2:
#     print('amenamecy', user3)
#     print('amenapoqry',user2)
# elif user3 > user2 and user2 > user1:
#     print('amenamecy', user3)
#     print('amenapoqry',user1)
# else:
#     print('havasar en')

# ------------------------------------------------

# 3. You have number. Write a python program which to print a new number with digits reversed as of original one.

# x = int(input('mutqagrel qaranish tiv----'))
# x1 = x % 10
# x2 = x // 10 % 10
# x3 = x // 100 % 10
# x4 = x // 1000
# print(f'{x1}{x2}{x3}{x4}')

# [:: -1]- nshanakum e reverse, nuyn xndiry kareli e lucel mi toxov:)

# print(input('enter number---')[::-1])


# ----------------------------------------------------

# shaxmati xndir

# tar1 = 'aceg'
# tar2 = 'bdfh'
# tar = input('(a-h)--->>>')
# tiv = int(input('(1-8)---->>>>'))
# if (tiv % 2 == 0 and tar in tar1) or (tiv % 2 != 0 and tar in tar2):
#     print('spitak')
# elif (tiv % 2 == 0 and tar in tar2) or (tiv % 2 != 0 and tar in tar1):
#     print('sev')

# -------------------------------------------

'''chingachungi xndir'''

# import random as r

# user = input('mutqagrel xaxaqary----')
# xax = 'mkrat', 'qar', 'tuxt'
# pc = r.choice(xax)
# print('pc xaxaqar', pc)
# if user == 'mkrat' and pc == 'tuxt':
#     print('user win')
# elif user == 'qar' and pc == 'mkrat':
#     print('user win')
# elif user == 'tuxt' and pc == 'qar':
#     print('user win')
# elif user == pc:
#     print('nichya')
# else:
#     print('pc win')

# ------------------------------------------------

# You (input) and pc have followers (pc have random followers) if your followers
# is great 20% than pc you are blogger otherwise pc is blogger.

# import random as r
# me = int(input('enter followers----'))
# pc = r.randint(1,100)
# if me >= pc + (pc * 20/ 100):
#     print('pc---',pc)
#     print('i am a blogger')
# else:
#     print('pc----',pc)
#     print('pc is blogger')
'''object-oriented programming'''
'''kodayin krknutyunic xusapelu u kody maximal optimal sarqelu hamara'''
'''kody ashxatuma aveli arag u apahov'''

# class Myclass:
#     x = 5
# print(Myclass.x)

'''funkcian ete grvuma class-i mej darnuma method'''
# class Myclass:
#     def __init__(self, x):
#         self.x = x

#     def func(self):
#         return self.x
    
# myclass = Myclass(5)
# print(myclass.func())




'''es jarangutyuna'''
# class Mard:
#     def __init__(self, fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#     def mardik(self):
#         return f'anun - {self.fname}, azganun - {self.lname}, tariq - {self.age}'
# # esi super classa
# x = Mard('Gevorg','Yesayan', 17)
# print(x.mardik())

# class cragravorox(Mard):
#     def __init__(self, fname, lname, age, komp):
#         super().__init__(fname,lname,age)
#         self.komp = komp
# # esel sub classa
#     def python(self):
#         return f'anun - {self.fname}, azganun - {self.lname}, tariq - {self.age}, komp - {self.komp}'

# class backend(cragravorox):
#     def __init__(self, fname, lname, age, komp, lezu):
#         super().__init__(fname, lname, age, komp)
#         self.lezu = lezu

#     def pyt(self):
#         return f'{self.fname} - {self.lezu}'

# z = backend('Gevorg','Yesayan',17, 'macbook', 'python')
# print(z.pyt())
# y = cragravorox('Gevorg','Yesayan',17, 'macbook')
# print(y.python())


'''sub class-y karuma ashxatacni ham ira methodnery ham super class-i methodnery'''
'''super class-y miayn ira meyhodnery'''



'''oop uni 4 jyux inkapsulyaciya, abstrakciya, polimorfizm, jarangutyun'''

# --------------------------OOP calculator-----------------------------


# class Calculator:
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2

#     def gumar(self):
#         return self.number1 + self.number2
    
#     def hanum(self):
#         return self.number1 - self.number2

#     def bajanum(self):
#         return self.number1 / self.number2

#     def bazmapatkum(self):
#         return self.number1 * self.number2
    

# x = Calculator(5,6)
# print(x.bazmapatkum())


# --------------------------OOP change-----------------------------

# Create a class Change:You have 3 methods in your class:
# Usd --- Eur
# Usd --- Amd
# Usd --- Ru


# class Change:
#     def __init__(self,usd):
#         self.usd = usd

#     def eur(self):
#         return self.usd / 1.25
    
#     def rub(self):
#         return self.usd * 77.5
    
#     def dram(self):
#         return self.usd * 478
    
# x = Change(500)
# print(x.eur())



'''es polymorphismov xndira'''
# import math as m
# class koxm:
#     def __init__(self,number):
#         self.number = number

# class erankyun(koxm):
#     def __init__(self,number):
#         super().__init__(number)

#     def makeres(self):
#         p = 3 * self.number / 2
#         return m.sqrt(p * (p - self.number) ** 3)


# class Qarakusi(koxm):
#     def __init__(self, number):
#         super().__init__(number)

#     def makeres(self):
#         return self.number ** 2
    
# class Shexankyun(koxm):
#     def __init__(self,number):
#         super().__init__(number)

#     def makeres(self):
#         return self.number ** 2
    
# x = erankyun(10)
# y  = Qarakusi(20)
# z = Shexankyun(30)
# print(x.makeres(), '\n', y.makeres(), '\n', z.makeres())


# ----------------------- OOP encapsulation ---------------------------
'''da class-i miji atributnerin sahmanapakum talna'''
'''kara lini private protected kam public'''
'''public-- hangist ogtagorcumenq class-ic durs'''


# esi publica
# class Myclass:
#     def _init_(self, res): 
#         self.res = res
# x = Myclass(10)
# print(x.res)

# protected
# class Myclass:
#     def __init__(self, res):
#         self._res = res
# x = Myclass(10)
# print(x._res)

# private
# class Myclass:
#     def __init__(self, res):
#         self.__res = res
# x = Myclass(10)
# print(x.__res)

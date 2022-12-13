#print(type(1))
#print(dir(1))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # def __str__(self):
#         #return f"Class info: name={self.name} age={self.age}"
#     def __repr__(self):
#         return f"Class info: name={self.name} age={self.age}"


# person = Person("behruz", 24)
# person = Person("Abror", 24)
# print(person)

# # import datetime
# # date = datetime.datetime.now()

# # print(date, repr(date))
# #print("213", str("123"), repr("213"))

# # print(dir(Person))

# class Number:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({0}, {1})".format(self.x, self.y)
    
#     def __sub__ (self, other):
#          x = self.x - other.x
#          y = self.y - other.y
#          return Number  (x, y )
    
   
# number = Number(5, 6)
# number_2 = Number(3, 5)
# print(number - number_2)
# number.x, number_2.y

# class Number:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     # def __str__(self):
#         # return "({0}, {1})".format(self.x, self.y)
    
#     def __sub__ (self, other):
#          x = self.x - other.x
#          y = self.y - other.y
#          return Number  (x, y )
    
   
# number = Number(5, 6)
# number_2 = Number(3, 5)
# print(number - number_2)
# number.x, number_2.y
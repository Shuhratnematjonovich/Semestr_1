"""Legb"""


# print(print)# built in
#
# name = "bexruz"# global

# def get_name():
#     name = "george"# local
#     print(name)

# get_name()


# modifying global variables
# name = "dave"

# def spam():
#     global name # импортируем глобалную переменную
#     name = "guido" # changes the global name above

# spam()
# print(name)


# def foo(items):
#     items.append(42)

# a = [1, 2, 3]
# foo(a)
# print(a)



# def bar(items):
#     items = [4, 5, 6]

# b = [1, 2, 3]
# bar(b)
# print('b ne pomenyalos', b)



# def parent():
#     a = 5 
#     return a

# print(" ne vlojenniy", parent())

# # local enclosed global builtin
# def parent():
#     a = 5
#     def answer():
#         return a
#     return answer()

# print(" vlojenniy", parent())    





# a = 20 
# def parent():
#     # enclosed
#     a = 5
#     def answer():
#         # local
#         a = 10
#         def get():
#             return a 
#         return get()
#     return answer()




# def outer():
#     # enclosed
#     x = "local"

#     def inner():
#         # local
#         nonlocal x
#         x = 'non local'
#         print('inner:', x)

#     inner()
#     print("outer:", x)

# outer()













































































































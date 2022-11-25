"""                  
1) PVM - это python virtual machine ,который виполняет исходный код передаваемый через байт код

схема: исходный код > байт код > PVM

2) str(stroki), int(seliyi chisla), bool(true,false), float(drobniyi chisla), list(spisok), tuple(kortej), set(mnojestva), 
frozenset, dict(slovar)

3)immutable - int, float,tupl, bool, set
  mutable - list, str, dict 
  immutable это не изменяемые переменные который хранятся по одним id ,
  mutable это изменяемые переменные который каждый раз для ных создается новый id

4) f' 'format

5)с помощью in можно проверит список кортеж словарь , если значения передаваемое с помощью In
  is проверяет является ли етим значением  


6) 4 oblasti (legb) # local enclosed global builtin

7) Да возвращает NONE

"""
# Задача №1 

# names = ["john", "artur","albert", "nik", "david", ]
# def name():
#   return max(names)


# print(name())

# names = ["john", "artur","albert", "nik", "david", ]
# def name(names):
#     for i in len(names):
        
#           return i
# print(len(name()))






# Задача №3

# words= "You've got that fire (fire). The flavor, the style (style)"

# list_2 = list()
# list_2.append(words)
# print(list_2)






# Задача №4

# names = [] 
# for i in range(10): 
#     names.append(i + 4) 
#     if i == 7: 
#        names.pop(0) 
#        continue  

# print(names)





# задача №5

# names = ["john", "artur","albert", "nik", "david", ]

# if "john" in names:
#     print("john")
# else:
#     print(-1)
    

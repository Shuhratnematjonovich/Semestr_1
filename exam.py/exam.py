"""
### Теория
1. Назовите все типы переменных и их особенности ?
1. int, str, bool, float, None, list, Tuple, set, frozenset:
list , set, dict это изменяемые типи переменных , осталные переменные не изменяемые .

2. Какие типы переменных можно хранить в качестве значений множества и ключа словаря ?
2.  Только неизменяемые типы  переменных.

3. Что такое MRO и наследование в питоне:



4. Опишите процесс публикования изменений в гитхаб ?
4. git add . или имя файла , git commit -m, git push 

5. В чем разница между функцией и методом ?
5. То что  создается внутри класса  називается методом . 

"""







'''
 ### Теория + Задачи
 # 1. Перечислите и Приведите пример оператов: сравнения, логических, особые операторы:
1. == , != , <= , >= , > , < .
для сравнения равно == (2 == 2), для сравнения не равно != 3 != 2 ,  для сравнения менше или равно 2 <= 3,  
для сравнения больше или равно 4 >= 3,  для сравнения больше 5 > 2, для сравнения меншье 2 < 3 .

and , or, not

And должны соблюдатся все условия (if 2 > 3 and 4 < 5) , OR   должна соблюдатся хотя бы одно из условий num == num_2 or num < num_3 
not для отрицания условия щтобы получить True если False . False если True. 

is,  is not , in , not in:
 
is щтобы сравнить значения id . a = 1, b = 1 : a is b (TRUE)
is not  щтобы получить True если False . False если True. a = 1, b = 1 : a is b (FALSE)

in щтобы проверит значения или переменную если она в итерируемом обьекте : 
names = [ john , li , forest] if john in names: print(True) .  else : print(False).

in not щтобы получить True если False . False если True. 
names = [ john , li , forest] if john not in names: print(True) .  else : print(False).

2 Что такое полиморфизм? приведите пример с полиморфизмом (надо создать свой пример):
2 . это когда работать с разными переменными по разному : пример print(1 + 1) print('hel'+ 'lo')



'''
# 3. Исправьте код. В конце вы должны создать код по проверке данных ползователя и возвращает сообщение об успешном или проваленном логине.
#```py
# def validate(username, password):
#     if  username ==  "Random" and password == "2321ewfsef":
#         return "Вы успешно вошли в систему!"
#     else: 
#         return "Пароль или имя пользователя не правильны"
    
# 4. Приведете список областей видимости в питоне и пример с каждым из них.
# 4  4 oblasti (legb) # local enclosed global builtin











#### Задачи
# N 1. Исправьте код ниже. После исправления код должен возваращть все аргументы,
#  которые были приняты в виде списка `other_info` и выводить их на экран:

# def get_data( code, salary,*args , **kwargs):
#     other_info = []
#     other_info.append(code)
#     other_info.append(salary)
#     for arg in args:
#         (other_info.append (arg))
#     for key, val in kwargs.items:
#            return other_info.append((key, val))

#     return other_info

# 22. Создать класс Gum, который описывает жевачку с атрибутами:#  smell, price, company, name, special_features, count и
#  с методом __str__, который возвращает информацию о жевачке со всеми атрибутами.
#  От класса Gum создать два других класса: Orbit и Trident.
#  Orbit должен иметь ещё один атрибут country (страна произвдства). 
# Trident должен иметь ещё один атрибут date_of_production (дата производства).

class Gum():
    def __init__(self, smell, price, company, name, special_features, count):
        self.smell = smell
        self.price = price
        self.company = company
        self.name = name 
        self.special_features = special_features
        self.count = count
    
    def __str__(self):
        return    "(smell gum:{0}, price gum: {1}), company gum:{2},name gum {3},special_features {4}, count{5}, ".format(self.smell, self.price, self.company, self.name, self.special_features, self.count )



gum = Gum()

class Orbit(Gum):
    def __init__(self, country):
        self.country = country

orbit = Orbit()


class Trident(Gum):
    def __init__(self, date_of_production):
        self.date_of_prouction = date_of_production



trident = Trident()












    













































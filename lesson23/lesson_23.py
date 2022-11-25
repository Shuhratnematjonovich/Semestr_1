# class PlayerCHaracter:
#     # class object attribute
#     membership = True # доступ для всех образов класса
#     def __init__(self,   name ="anonymus", age = 0):
#         #if age > 18 
#         self.name = name # attributes
#         self.age = age
#         # self._hooby = hobby
#     #     def _welcome(self);
#     #     return "hey"
#     # def shout(self): # metod
#     #     return f"my name is {self.name}"
        
#     @classmethod 
#     def adding_things_2(cls, num1, num2): #cls eto kak self
        
#         return cls(num1 + num2)
#     #  @staticmethod     metod dlya ispolzovaniya bez self ili silki
#     #  def multiply(a,b)
#     #   return a * b

# player_1 = PlayerCHaracter("jerry", 20)
# print(player_1.name, player_1.age)
# player_1 = PlayerCHaracter("jon")
# print(player_1.name, player_1.age)

# player_3 = PlayerCHaracter.adding_things_2(2,20) 
# print(player_3.age, player_3.name)





#print(player_1.adding_things(2, 5))

"""
Encapsulation (Инкапсуляция) - в информатике размещение в одном компоненте данных и методов,
 которые с ними работают.Также может означать скрытие каких-то данных, чтобы их не могли изменить или удалить.
 Например, доступ к скрытой переменной может предоставляться не напрямую,  
 а с помощью методов для чтения и изменения её значения.

"""
"   _   eto dlya sozdaniya skritogo atributa ili metoda" 


# print(player_1._welcome()) nelzya tak pisat

"""draft - вес корабля 
crew - пассаижры 
 
is_worth_it - создать метод, который возвращает True или False, если  
вес корабля после того как вычесть количество пассажиров остается  
равным 20 или больше, то вы возвращете True (его можно грабить) 
каждый пассажир (crew) добавляет в вес корбался 1.5 единиц"""


class Ship: 
    def __init__(self, draft, crew): 
        self.draft = draft 
        self.crew = crew
        
    def is_worth_it(self):
        if self.draft - self.crew * 1.5 >= 20:
            return True
        else:
           return False

Titanic = Ship(45,15)

print(Titanic.is_worth_it())

















































































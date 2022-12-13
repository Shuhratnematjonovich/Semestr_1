# class Human:

#     # Статические поля
#     default_name = input("enter your name:")
#     default_age = int(input("enter your age:"))
    
#     def __init__(self, name=default_name, age=default_age):
#         # Динамические поля
#         # Публичные
#         self.name = name
#         self.age = age
#         # Приватные
#         self.__money = 0
#         self.__house = None

#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')
# human = Human()

# # print(human.name, human.age)


scones = {
    "Фрукты": 22,
    "Пустая": 14,
    "Корица": 4,
    "Сыр": 21
}
print(scones)

scones["Вишня"] = 10
print(scones)
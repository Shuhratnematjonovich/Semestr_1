# # # # iterable Это те переменные , которые хранят больше одного значения

# # # # Dictionary
# # # # Ключом словаря могут быть только не изменяемые типы переменных

# # # from tkinter.messagebox import NO


# # # user_data = {
# # #     "ключь": "значение",
# # #     1: None,
# # #     2: 21,
# # #     3: 6.7,
# # #     4: [2,3,4],
# # #     5: (1,2,3),
# # #     6: {"key": "Другой словарь"}
# # #     # [1]: 23, # error
# # #     # (2,3, [2,3]):"error" # кортеж можно использовать как ключь б но не рекомендуется
# # # }
# # # # print(type(user_data), user_data, user_data["ключь"], sep="\n")


# # # user_data = {
# # #     "1": "string",
# # #     2: None,
# # #     3: 45,
# # #     4: 4.5,
# # #     5: (),
# # #     6: {},
# # #     7: []
    
# # # }

# # # print(user_data)


# # user_data = {
# #     "username": "gobby",
# #     "password": "231354ldsc",
# #     "age": 25
# # }
# # print(user_data["age"])



# # user_data_2 = {
# #     "username": "gobby",
# #     "password": "231354ldsc",
# #     "age": 25
# # }


# # user_data = [ 
# #     {
# #         "username": "gobby",
# #         "password": "231354ldsc",
# #         "age": 25
# #     },
# #     {
# #         "username": "gobby",
# #         "password": "231354ldsc",
# #         "age": 25
# #     },
# # ]    

# # print( user_data[0]["username"], user_data[0]["age"])


# # print(user_data.keys(), user_data.values(), user_data.items(), sep="\n")

# # user_list = list(user_data.values())
# # print(user_list)
# # print( user_data.get("age", user_data.get("unexisting")))


# # set - множество
# # нельзя индексироват
# # можно менять через методы или циклы 
# from os import remove


# numbers = {2,3,4, "hello", 2, 4}
# print(numbers)

# numbers = {} # dict
# print(type(numbers))
# numbers = set()
# print(type(numbers))

# remove_duplicates = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, "AA", "bb", "AA"]
# print( remove_duplicates, set(remove_duplicates), sep="\n")

# # print(remove_duplicates, list(remove_duplicates),  )





































































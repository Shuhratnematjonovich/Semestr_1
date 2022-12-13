# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f' i am a cat. My name is {self.name}. I am {self.age} years old')

#     def make_sound(self):
#         print("Meow")


# class Dog:
#      def __init__(self, name, age):
#         self.name = name
#         self.age = age

#      def info(self):
#         print(f' i am a dog. My name is {self.name}. I am {self.age} years old')

#      def make_sound(self):
#          print("Bark")

# cat1 =Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound

"""Дз 
1. Создать класс с атрибутами: name, email, password, purchases (список), card 
методами: 
- purchase - метод для покупки товаров. 
- register - создать нового пользователя и включить его в список пользователей. 
    name - должен содержать только буквы 
    email - должен содержать @ 
    password - миинмальная длинна 6 
    card - длина ключа code была равна 16 
- login - вход в систему, если пользователь уже есть. При этом пользователь должен иметь все свои данные:  
    покупки, список игр и т.д 
- add_product - добавить куплейнный товар в атрибут purchases"""


# class Market:
#     def __init__(self,name, email, password, purchase, card):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.purchase = purchase
#         self.card =  card

#     def __register__(self):
        
#         if self.name == str and "@" in self.email and self.password > 6 and self.card == 16:
            
#             print("you have successfully registred: ")
#         else:
#             print("you have not registred , try again please: ")       
#     def __login__(self):





















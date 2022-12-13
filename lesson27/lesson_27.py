# USERS = [
#     {
#     "name":"behruz",
#     "password":"6660444",
#     "email": "@65656",
#     "purchase": [],
#     "card": {"code": 56565656565, "balance":1000  }

#      }
#      ]
# products = []

# class Store:
#     purchase = []

#     def __init__(self, name, email, password, card_code, card_balance):
    
#         self.name = name
#         self.email = email
#         self.password = password
#         self.cardcode = card_code
#         self.card_balance =  card_balance

#     @classmethod
#     def register(cls, name, email, password, card_code, card_balance):
#         for user in USERS: 
#             if user["email"] == email or user["password"] == password:
#                 return "wrong email or password."
#             else:
#                 break
        
#         if not(name and email and password and card_code and card_balance):
#             return "Empty values were given."

#         if name.isalpha() and "@" in email and len(password) >= 6 and len(card_code) == 16:
#                 USERS.append(
#                     {
#                         "name":name,
#                         "password": password,
#                         "email": email,
#                         "purchase": [],
#                         "card": {"code": card_code, "balance": card_balance }

#                     }
#             )
#                 return cls(name, email, password, card_code, card_balance)
#         else:
#             return "wrong credentials."      


#     # @classmethod
#     # def login(cls, email, password):
#         # for user in USERS:
#             # if user["email"] == email and user["password"] == password:

# enter_metod = input("choose method: register or login:")
# if enter_metod == "register":
#     user_1 = Store.register("behruz", "behruz@gmail.com", "214tgdfsa","8600021024528732", 1000)
# elif enter_metod == "login":
#     user_1 = Store.login("behruz", "behruz@gmail.com", "214tgdfsa","8600021024528732", 1000)
# print(user_1)
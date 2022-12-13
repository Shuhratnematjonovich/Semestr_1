



Users = [{
    
     
}]




class Market:
    # default_name = input("enter your name :")
    # default_email = input("enter your email adress :")
    # default_password = input("enter your password :") 
    # default_card = int(input("enter your card number :"))   
    # default_purchase = input("enter your purchase :")
    # purchaseshu
    
    # def __init__(self,name, email, password, card):
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     # self.purchase = purchase
    #     self.card =  card

    def __register__(self,name=input("enter name:"), email=input("enter email:"), password=input("enter password:"),card=input("enter card:")):
        self.name = name
        self.email = email
        self.password = password
        self.card =  card
        if name.isalpha()  and "@" in self.email and self.password > 6 and self.card == 16:
            print("you have registred ")       
        
        #  Users ["name"] = self.name 
        #  Users ["email"] = self.email  
        #  Users ["password"] = self.password
        #  Users ["card":] = self.card   
        else:
            print("you have not registred , try again please: ")       
    # def __login__(self):
    
market = Market()
Users = [{
    }]

print(market.__register__())
 
    
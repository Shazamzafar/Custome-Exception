#Name:      Shazam Zafar
#Class:     Python (M5L5)
#Date:      November 29, 2018


#list for all the data given
#First letter of the flavor needs to be capital

flavors = ['Vanilla','Chocolate','Strawberry','Mint','Pistachio','Spumoni']
scoops = [1,2,3]
Itype = ['cone','bowl']

#Exceptions Class
class FlavorError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

#Exceptions Class        
class ScoopsError(ValueError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

#Creating menu class for IceCream store
class IceCreamStore:
        def __init__(self, flavor, scoop, Itype): 
            self.__flavor = flavor
            self.__scoops = scoop
            self.__Itype = Itype
        
        #creating class for flavor, scoop and type 
        def set_falvour(self, flavor):
            self.__flavor = flavor

        def set_scoop(self, scoop):
            self.__scoops = scoop
        
        def set_type(self, Itype):
            self.__Itype = Itype
        
        #calling the flavor, scops and type
        def get_falvour(self):
            return self.__flavor

        def get_scoop(self):
            return self.__scoops

        def get_type(self):
            return self.__Itype
    
# loop asking user again and again

while True:
    #Asking user for input
    flavor =input("Enter a flavor of ice cream: ")
    Scoops = (input("Enter the number of scoops "))
    Type = (input("Would you like a cone or bowl? "))
    myIceCream = IceCreamStore(flavor,Scoops,Type)
    excount = 0
    #Exceptions for flavor
    try:
        if myIceCream.get_falvour() not in flavors.__str__():
            raise FlavorError('{0} is not on the menu.'.format(myIceCream.get_falvour()))
    except FlavorError as e:
        print(e.strerror)
        excount+=1
    #Exception for scoops
    try:
        if myIceCream.get_scoop() not in scoops.__str__():
            raise ScoopsError('we do not offer that many scoops')
    except ScoopsError as e:
        print(e.strerror)
        excount+=1
    # printing the final output
    if excount <=0:
        print(Scoops,"Scoops of", flavor, "in a",Type)
    print()


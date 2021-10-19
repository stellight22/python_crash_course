class Revision():

    def __init__(self, number, city):
        self.number = number
        self.city = city
    
    def basic_method(self):
        print(self.number)

    def print_country(self):
        print(self.city)

    def anything_is_possible(self):
        pass

    def function():
        print("not accessible without self")

    function() # can be called within class but not outside
    # jj = Revision(6)
    #cannot create an instance of the class inside the class itself



revi = Revision(6, 'Jakarta')
Revision.function()
#outputs not accessible without self

revioli = Revision(7,'Seoul')
ramen = Revision(8, 'Beijing')

revioli.basic_method()
revioli.print_country()

ramen.basic_method()
ramen.print_country()




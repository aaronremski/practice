## Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”
class Budget:

    categories = ['food','clothing','entertainment','health','housing','auto','income']
    # Instantiate with 0 balance
    def __init__(self, category, category_balance=0, category_list=categories, balance=0):
        self.balance = balance
        self.category = category
        self.category_balance = category_balance
        self.category_list = category_list


    # Method for circle

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2



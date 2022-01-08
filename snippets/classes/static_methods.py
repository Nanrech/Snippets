class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    def sayHi(self):
        print(f'hi, i have {self.toppings}')

    @staticmethod
    def validate(topping_singular):
        if topping_singular == 'pineapple':
            raise ValueError('¡No pinapels!') # This would raise an error, stopping the program
        else:
            return True

ingredients = ['tomate', 'carbonara', 'a']

if all(Pizza.validate(i) for i in ingredients):
    pizza = Pizza(ingredients)

# Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.

pizza.sayHi()

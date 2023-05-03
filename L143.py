#Emliy Nixon and Katie O'Rourke
class coffee:
    """Represents a liquid and object with dimensions.
    Attributes: Amount, mug color, coffee type, coffee additives"""

coffee.amount = 300 
coffee.mugcolor = "blue"
coffee.coffeetype = "Arabian"
coffee.coffeeadd = "Cream, sugar"

def coffee_drinking_simulation(amount):
    Remaining = coffee.amount - amount
    
    if Remaining > 0:
        print("There is", Remaining, "mL of coffee left.")
    else:
        print("There is no more coffee left.")

coffee_drinking_simulation(256)
coffee_drinking_simulation(300)


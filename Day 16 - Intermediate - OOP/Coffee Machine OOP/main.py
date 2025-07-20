from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

menu_items = menu.get_items()

money_machine.report() #print report of how much money is in the machine
coffee_maker.report() # print report of resources in the coffee maker

# enough_resources = coffee_maker.is_resource_sufficient() #check if there are enough resources to make the drink, returns True or False
# payment_successful = money_machine.make_payment() # Returns True or False depending on whether the payment was successful


# if enough_resources and payment_successful:
#     make_drink = coffee_maker.make_coffee() #make the drink if there are enough resources and payment was successful



is_on = True
while is_on:
    choice = input(f"What would you like? {menu_items}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_choice = menu.find_drink(choice)
        print(drink_choice)
        if coffee_maker.is_resource_sufficient(drink_choice):
            drink_cost = drink_choice.cost
            if money_machine.make_payment(drink_cost): #returns True if payment was successful and adds the money to the machine profit or total
                coffee_maker.make_coffee(drink_choice) #use was able to pay so we make the coffee
#                     coffee_maker.make_coffee(drink)
#             else:
#                 print("Please choose a valid option.")


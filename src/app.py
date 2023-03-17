import budget
from budget import Budget


food = budget.Budget("Food")
housing = budget.Budget("Housing")
utilities = budget.Budget("Utilities")
transportation = budget.Budget("Transportation")
travel = budget.Budget("Travel")

food.deposit(200, "Initial Deposit")
housing.deposit(700, "Initial Deposit")
utilities.deposit(200, "Initial Deposit")
transportation.deposit(400, "Initial Deposit")
travel.deposit(50, "Initial Deposit")

food.withdrawal(30.25, "Groceries Meijer")
utilities.withdrawal(50, "Columbia Gas")
utilities.withdrawal(30, "Water")
transportation.withdrawal(30, "Gas @ Costco")
food.withdrawal(26.54), "Culvers"

food.deposit(200, "20230317 Paycheck")
housing.deposit(700, "20230317 Paycheck")
utilities.deposit(200, "20230317 Paycheck")
transportation(200, "20230317 Paycheck")
travel.deposit(50, "20230317 Paycheck")

housing.withdrawal(1350, "House Payment")
food.withdrawal(96.84, "Groceries Costco")
utilities.withdrawal(200, "Electric")
food.transfer(25, travel)

print(food)
print(travel)
print(utilities)






















# class Budget:

#   def __init__(self, activity_name, menu_options, print_menu, option):
#       self.activity_name = activity_name
#       self.menu_options = []
#       self.print_menu = print_menu
#       self.option = option


# menu_options = {
#   1: "Balance",
#   2: "Deposit",
#   3: "Withdrawal",
#   4: "Transfer",
#   5: "Ledger",
#   6: "New Budget",
#   7: "Exit",
# }

# def print_menu():
#   for key in menu_options.keys():
#     print(key, "--", menu_options_[key])

# def option1():
#   print("Handle option \"Balance\"")
# def option2():
#   print("Handle option \"Deposit\"")
# def option3():
#   print("Handle option \"Withdrawal\"")
# def option4():
#   print("Handle option \"Transfer\"")
# def option5():
#   print("Handle option \"Ledger\"")
# def option6():
#   print("Handle option \"New Budget\"")
# def option7():
#   print("Handle option \"Exit\"")

# if __name__ == "__main__":
#   while (True):
#     print_menu()
#     option = " "
#     try:
#       option = int(input("Please Enter the number for the activity you wish to initiate: "))
#     except:
#       print("Wrong input type. Please enter a number...")
#       # Check choice and initiate activity selected
#       if option == 1:
#         option1()
#       elif option == 2:
#         option2()
#       elif option == 3:
#         option3()
#       elif option == 4:
#         option4()
#       elif option == 5:
#         option5()
#       elif option == 6:
#         option6()
#       elif option == 7:
#         option7()
#       else:
#         print("Invalid option. Please enter a number between 1 and 7")

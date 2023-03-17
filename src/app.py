from budget import Budget


print()


























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

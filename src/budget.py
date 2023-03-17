

######## CLASS ########
class Budget():
  print("********************** MY BUDGET  ********************************")

  def __init__(self, name):
    self.ledger = []
    self.name = name
    self.balance = 0
    self.withdrawal = 0

  def deposit(self, amount, description=''):
    self.balance += (float(amount))
    self.ledger.append({"amount": (float(amount)), "description": description})

  def withdrawal(self, amount, str(description='') -> str):
    if self.check_funds(float(amount)):
      self.balance -= (float(amount))
      self.withdrawal += (float(amount))
      self.ledger.append({"amount": -(float(amount)), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance 

  def transfer(self, amount, other):    
    if self.check_funds(float(amount)):
      self.withdrawal((float(amount)), f"Transfer to {other.category}")
      other.deposit((float(amount)), f"Transfer to {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    if self.balance < (float(amount)):
      return False
    else:
      return True  

  def __str__(self):
    output = self.name.center(30, "*")    

    for item in self.ledger:
      output +=  '\n' + item['description'][30].ljust(30) + f"{item['amount']:.2f}".rjust(8)

      output += '\n' + f"Total: $ {round(self.balance, 2)}"

      return output



# budget1 = Budget("Food")
# budget2 = Budget("Housing")
# budget3 = Budget("Utilities")
# budget4 = Budget("Transportation")
# budget5 = Budget("Travel")






  # def ask_budget_name(self):
  #   new_budget_name = input("Enter a name for the new budget: ")
  #   return new_budget_name


# if __name__ == '__main__':
#   Budget()

    # return(new_budget)
    # print("A new budget for,", budget_name, "has been created.")

  # def get_budget_name(self):
  #   get_budget_name = input('''*************** MY BUDGET *************** 
  #   Enter name of new budget: ''')
  #   get_budget_name = budget_name.append
  #   return print("A new budget for,", get_budget_name, "has been created.")

# budget_name = ()

# print(budget_name1)


    # self.my_budgets = my_budgets.set(**kwargs)

    # print(my_budgets)






































######## CLASS ATTRIBUTES ########
######## CLASS METHODS ########
######## INSTANCE ATTRIBUTES, METHODS and PROPERTIES ########
  # def __init__(self, activity_name):
  #   self.activity_name = "activity_name"
  #   self.menu_options = "menu_options"
  #   self.print_menu = "print_menu"
  #   self.option = "option"

  #   self.activity_balance = "get_balance"
  #   self.activity_deposit = "deposit"
  #   self.activity_withdrawal = "withdrawal"
  #   self.activity_transfer = "transfer"
  #   self.activity_ledger = "leger"
  #   self.activity_new_budget = "new_budget_category"  
  # @property  
  # def get_activity_name(self):
  #   activity_question = input("What would you like to do today? ")
  #   return(activity_name)
  # @property_name.setter
  # def activity_name.(self, )
  
  
  # def set_activity_name(self):

  #   initiate_activity_name
  # def new_budget_category(self):  
  #   self.budget_name = "budget_name"
  #   self.get_Name = "budget_name"
  #   input("Enter the name of the new budget category you wish to create: ")
  #   self.initial_deposit_amt = "initial_deposit_amt"

    
  #   self.update_balance = "update_balance"

  # def get_balance(self):
  #   self.current_balance = "current_balance"

  # def check_funds(self):
  #   self.enough_for_withdrawal = "enough_for_withdrawal"    
  
  # def deposit(self):
  #   self.deposit_amt = "deposit_amt" 
  #   self.deposit_desc = "deposit_desc" 
  #   self.deposit_to = "deposit_to"
    
  # def withdrawal(self):
  #   self.withdrawal_amt = "withdrawal_amt"
  #   self.withdrawal_desc = "withdrawal_desc"
  #   self.withdrawal_from = "withdrawal_from"

  # def transfer(self):
  #   self.transfer_from = "transfer_from"
  #   self.transfer_to = "transfer_to"
  #   self.transfer_amt = "transfer_amt"

    

######## OBJECTS ########    



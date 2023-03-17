######## CLASS ########
class Budget:

######## CLASS ATTRIBUTES ########

######## CLASS METHODS ########

######## INSTANCE ATTRIBUTES, METHODS and PROPERTIES ########
  def __init__(self):
    self.name = "name"
    self.initial_deposit_amt = "initial_deposit_amt"
    self.current_balance = "current_balance"

  def get_balance(self):
    self.current_balance = "current_balance"

  def check_funds(self):
    self.enough_for_withdrawal = "enough_for_withdrawal"    
  
  def deposit(self):
    self.deposit_amt = "deposit_amt" 
    self.deposit_desc = "deposit_desc" 
    self.deposit_to = "deposit_to"
    
  def withdrawal(self):
    self.withdrawal_amt = "withdrawal_amt"
    self.withdrawal_desc = "withdrawal_desc"
    self.withdrawal_from = "withdrawal_from"

  def transfer(self):
    self.transfer_from = "transfer_from"
    self.transfer_to = "transfer_to"
    self.transfer_amt = "transfer_amt"

######## INSTANCE VARIABLE ########    
    self.ledger = []    

######## OBJECTS ########    



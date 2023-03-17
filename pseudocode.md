# BUDGET APP

## CLASSES

- Budget

### CLASS ATTRIBUTES, METHODS and PROPERTIES

### INSTANCE ATTRIBUTES, METHODS and PROPERTIES

- **budget_category_name**
  - set name value
    - input "Enter the name of the new budget category you want to create: "
    - output "You have created a new budget category named: "
- **initial_deposit_amt**
  - get initial deposit -
    - input "Enter the amount you wish to deposit: "
  - set initial deposit amt value
    - get name of where to assign initial deposit
      - input "Which budget category do you want to deposit this to? "
      - set initial deposit amt of that budget category
- **current_account_balance**
  - set current_account_balance
    - defaults to initial_deposit_amt
    - updates due to deposits and withdrawals
  - get_current_balance  
- **deposit_budget_category_name**
  - get deposit_budget_category_name
    - input "Which budget category do you want to make a deposit to? "
  - set deposit_budget_category_name
- **deposit_amt** (must be a positive number)
  - get deposit amt
    - input (Enter deposit amount: $)
  - set deposit amt
    - set deposit value
- **deposit_desc** (defaults to blank if nothing is entered)
  - get deposit description
    - input "Enter deposit description: "
  - set deposit description
- **withdrawal_budget_category_name**
  - get withdrawal_budget_category_name
    - input "Which budget category do you want to make a withdrawal from? "
  - set withdrawal_budget_category_name 
- **withdrawal_amt**
  - get withdrawal_amt
    - input "Enter amount you wish to withdrawal: $"
  - set withdrawal_amt
- **check_funds** (checks to see if a category has an entered amount available)
  - if there is money enough to cover the amount it will return true, else false
- **withdrawal_desc**
  - get withdrawal_desc
    - input "Enter withdrawal description: "
  - set withdrawal_desc  
- **update_balance**
  - get current_balance for withdrawal_budget_category_name
  - set current_balance 
    - current_balance - withdrawal_amt
- **transfer_withdrawal_budget_category_name**
  - get transfer_withdrawal_budget_category_name
    - input "Name of category you wish to transfer (withdrawal) money FROM: "
  - set transfer_withdrawal_budget_category_name  
- **transfer_deposit_budget_category_name**
  - get transfer_deposit_budget_category_name*
    - input "Name of category you wish to transfer (deposit) money TO: "
  - set transfer_deposit_budget_category_name*
- **transfer_amt**
  - get transfer_amt
    - input "Enter amount you wish to transfer: $"
  - set transfer_amt
- **check_funds** (checks to see if a category has an entered amount available)
  - if there is money enough to cover the amount it will return true, else false
- **transfer_desc**
  - get transfer_desc
    - input "Enter transfer description: "
  - set transfer_desc 
- **update_balance**
  - get current_balance for withdrawal_budget_category_name
  - set current_balance 
    - current_balance - transfer_amt
- **update_balance**
  - get current_balance for deposit_budget_category_name
  - set current_balance 
    - current_balance + transfer_amt

### INSTANCE VARIABLE

- **ledger**
  - get budget_category_name
    - input "Enter budget you wish to view the leger of: "
  - set   

budget_category_name = '''************** budget_category_name *************
initial deposit

print(budget_category_name)

print(************** Category Name *************)



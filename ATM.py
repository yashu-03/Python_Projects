# define the functions for the ATM
def check_balance(balance):
  print("Your current balance is: $" + str(balance))

def deposit(balance):
  amount = float(input("Enter amount to be Deposited: "))
  balance += amount
  print("\n Amount Deposited: $", amount)
  print("\n Your Updated Balance is: $", balance)
  return balance

def withdraw(balance):
  amount = float(input("Enter amount to be Withdrawn: "))
  if balance >= amount:
    balance -= amount
    print("\n You have Withdrawn: $", amount)
    print("\n Your Updated Balance is: $", balance)
  else:
    print("\n Insufficient balance  ")
  return balance

def change_pin(pin):
  new_pin = input("Enter your new 4-digit PIN: ")
  if len(new_pin) == 4 and new_pin.isdigit():
    pin = new_pin
    print("Your PIN has been changed successfully.")
  else:
    print("Error: Please enter a 4-digit PIN.")
  return pin

# main program
balance = 1000.0
pin = "1234"

while True:
  print("Welcome to the ATM!")
  print("Please enter your 4-digit PIN: ")
  user_pin = input()
  if user_pin == pin:
    while True:
      print("\n What would you like to do?")
      print("1. Check balance")
      print("2. Deposit money")
      print("3. Withdraw money")
      print("4. Change PIN")
      print("5. Exit")
      choice = int(input())
      
      if choice == 1:
        check_balance(balance)
      elif choice == 2:
        balance = deposit(balance)
      elif choice == 3:
        balance = withdraw(balance)
      elif choice == 4:
        pin = change_pin(pin)
      elif choice == 5:
        print("Thank you for using the ATM. Have a great day!")
        break
      else:
        print("Error: Please choose a valid option (1-5)")
  else:
    print("Error: Incorrect PIN. Please try again.")

# Add function
def add (n1, n2):
  return n1 + n2

# Substract function
def substract (n1, n2):
  return n1 - n2

# Multiple function 
def multiple (n1, n2):
  return n1 * n2

# Divide function
def divide (n1, n2):
  return n1 / n2

# Create a dictionary
calculator_dictionary = {
  "+": add,
  "-": substract,
  "*": multiple,
  "/": divide
}

### Recursion for fresh start again

def calculator():


  # Ask user to input
  num1 = float(input("What is the first number?: "))
  
  for symbol in calculator_dictionary:
    print(symbol)
  operation_symbol = input(" Pick an symbol from the line above : ")
  num2 = float(input(" What is the second number?: "))
  
  
  calculation_function = calculator_dictionary[operation_symbol]
  first_answer = calculation_function(num1,num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  
  ##### Multiple operation
  multiple_operation = True
  
  while multiple_operation:
    choice = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to new calculation : ").lower()
    if choice == "y":
      new_operation = input("Pick an operation: ")
      num3 = float(input("What is the next number?: "))
      calculation_function = calculator_dictionary[new_operation]
      second_answer = calculation_function(first_answer, num3)
      print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    else:
      multiple_operation = False
      calculator()

calculator()

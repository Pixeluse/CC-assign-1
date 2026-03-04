def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if b==0:
    return "Error:Cannot divide by 0"
  return a/b

def Calculator():
  """Main calculator Function"""
  print("=" * 40)
  print("simple calculator")
  print("=" * 40)
  print("Select Operation:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Exit")
  print("=" * 40)

while true:
  choice = input("\nEnter operation (1/2/3/4/5):")

if choice == '5';
print("Thank you for using the calculator")
break

if choice in ('1','2','3','4')
try:
  num1 = (float(input("Enter First number:"))
  num2 = (float(input("Enter Second number:"))

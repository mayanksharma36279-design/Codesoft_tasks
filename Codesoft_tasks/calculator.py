print("SIMPLE CALCULATOR")
print("1.Add")
print("2.Subtract")
print("3.MUltiply")
print("4.DIvide")
ch=float(input("Enter our choice:"))
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
if ch == 1:
    print("Sum is ",num1+num2)
elif ch == 2:
    print("Subtraction is ",num1-num2)
elif ch == 3:
    print("Multiplication is ",num1*num2)
elif ch == 4:
  if(num2!=0):
    print("Division is ",num1/num2)
  else:
    print("Division by zero is not possible")
else:
     print("Invalid Choice!")
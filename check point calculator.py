def calculator(num1, num2):
    
 operator = input ("enter the operator (+,-,/,*): ")

 if operator == "+":
        return num1 + num2
 
 elif operator == "-":
        return num1 - num2
 
 elif operator == "*":
         return num1 * num2
 
 elif operator == "/":
       
  if num2 == 0:
       return "Error: can not use"
  return num1 / num2

 else:
        return "Invalid operator"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator (num1, num2)
print("The result is: ", result)

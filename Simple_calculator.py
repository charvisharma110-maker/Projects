
a= float(input("Enter the first number : "))
b= float(input("Enter the Second number : "))
operation=input("Enter the operation to be performed ( + , - , * , / , avg ) : ")
if operation=='+':
    print("The sum is : ",a+b)
elif operation=='-':
    print("The difference is : ",a-b)
elif operation=='*':
    print("The product is : ",a*b)
elif operation=='/':
    if b!=0:
        print("The quotient is : ",a/b)
    else:
        print("Division by zero is not allowed.")
elif operation=='avg':
    print("The average is : ",(a+b)/2)  
else:
    print("Invalid operation entered.") 
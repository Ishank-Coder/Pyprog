def script():
   # Program make a simple calculator that can add, subtract, multiply and divide using functions
   import math
   # This function adds two numbers 
   def add(x, y):
      return x + y

   # This function subtracts two numbers 
   def subtract(x, y):
      return x - y

   # This function multiplies two numbers
   def multiply(x, y):
      return x * y

   # This function divides two numbers
   def divide(x, y):
      return x / y

   # This function represent number in exoponent
   def exponent(x,y):
      return x**y 

   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Exponent")
   print("6.square root")
   print("7.square")
   print("8.sin")
   print("9.cos")
   print("10.tan")
   print("11.factorial")
   print("12.log")
   # Take input from the user 
   choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12):")

   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number(*if you are finding square or square root of number then enter the number in first time and in second simply enter 1): "))

   if choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))

   elif choice == '5':
      print(num1,"**",num2,"=", exponent(num1,num2))

   elif choice == '6':
      print(num1,"under root","=",math.sqrt(num1))

   elif choice == '7':
      print(num1,"**",2,"=",(num1**2))

   elif choice == '8':
      print("sin",num1,"/",num2,"=",math.sin(num1/num2))

   elif choice == '9':
      print("cos",num1,"/",num2,"=",math.cos(num1/num2))

   elif choice == '10':
      print("tan",num1,"/",num2,"=",math.tan(num1/num2))

   elif choice == '11':
      fact=1
      kl=1
      while(kl <= num1):
         fact=fact*kl
         kl=kl+1
      print("The factorial of " ,num1, "=", fact)

   elif choice == '12':
       if (num2 == 1):
           print("log",num1,"=",math.log(num1))
       else:
           print("log",num1,"*",num2,"=",math.log(num1*num2))
        
   else:
      print("Invalid input")
   restart = input("Would you like to calculate more?")
   if restart == "yes" or restart == "y":
        script()
   if restart == "n" or restart == "no":
        print(" Goodbye.")
script()

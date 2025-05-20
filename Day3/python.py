#Write a function that takes a name as input and returns a personalized greeting.
s=input()
print(f"Welcome to python {s}")


#Implement a function to convert Celsius to Fahrenheit.
f=int(input())
c=(f-32)*(5/9)
print(f"Celsius temperature is {c:.2f}")

#Create a function that takes a list of numbers and returns their average.
l1=list(input().split(" "))
sum=0
for n in l1:
  sum+=int(n)
print(sum/len(l1))

#Create a menu-driven calculator using functions for add, subtract, multiply, and divide.
option=input("1.add\n2.sub\n3.multiply\n4.divide")
a=int(input())
b=int(input())
print("\n")
if option=="1":
  print(a+b)
elif option=="2":
  print(a-b)
elif option=="3":
  print(a*b)
elif option=="4":
  print(a/b)

#Write a program to print the multiplication table of a given number using a for loop.
m=int(input("provide number for multiplication\n"))
for i in range(1,11):
    product=(m*i)
    print(f"{m} * {i} ={product}")

# print("Hello World")
# a=input("Enter value=")
# print(a)

# c=input("Celsius: ")
# c=float(c)
# f=(c * 9/5)+ 32
# print('Farenheit: ',f)

# f=input("Farenheit: ")
# f=float(f)
# c=(f  - 32) * 5/9
# print('Celsius: ',c)

p=input('Enter principle amount: ')
r=input('Enter intrest rate: ')
t=input('Enter time yearly: ')
p=float(p)
r=float(r)
t=float(t)

simpleIntrest = (p * r * t)/100

print('SI = ', simpleIntrest)

print('Your total = ', p+simpleIntrest)

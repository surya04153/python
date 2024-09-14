print("Hello, World!")
def square(x):
    'Returns square of a number.'
    return x**2

def getName():
    return "suryanarayan Panda"
# Input: two numbers
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))

# Add the two numbers
#sum1 = num1 + num2

# Output the result
#print("The sum of", num1, "and", num2, "is:", sum1)

#age= int(input("Enter your age:"))
age = 15
if age>18 :
    print("sabalaka")
else:
    print("nabalaka")

lst = ["apple","orange","cucumber"]

for item in lst :
    print(item)

unique_numbers = {1, 2, 3, 4}  # set
print(type(unique_numbers))  # Output: <class 'set'>

summ=0
# Looping over a range of numbers
for i in range(1, 6):  # Loops from 1 to 5
    summ= summ +i
    summ=summ-1
print("Number:", summ,age)

print(square(5))

print("Length of your name:",len(getName()))
c= None
print(type(c))

x = [6, 3, 1]
s = iter(x)
print(next(s))      # -> 6
print(next(s))      # -> 3
print(next(s))      # -> 1
#print(next(s))      # -> StopIteration Error

x = [6, 3, 1]
y = [ i+2 for i in x ]   # List Comprehension expression
print(y)              # -> [36, 9, 1]





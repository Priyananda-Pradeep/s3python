# 1. Display your name
print("Priyananda Pradeep")
# 2. Display today's date
from datetime import date
print(date.today())
# 3. Create a variable city and display the sentence
city = "kozhikode"
print("I live in", city)
# 4. Create variables length and width. Calculate the area of a rectangle.
length = 10
width = 5
area = length * width
print("Area =", area)
# 5. Ask the user to enter their age and display it.
age = int(input("Enter your age:"))
print("Your age is", age)
# 6. Ask the user to enter two numbers and display their sum.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)
# 7. Calculate Simple Interest
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = (principal * rate * time) / 100
print("Simple Interest =", si)
# 8. Create variables of different data types
a = 10
b = 10.5
c = "Python"
d = True

print(a)
print(b)
print(c)
print(d)
# 8. Create variables of different data types
a = 10
b = 10.5
c = "Python"
d = True

print(a)
print(b)
print(c)
print(d)
# 9. Enter a decimal number and display its data type
num = float(input("Enter a decimal number: "))
print(type(num))
# 10. Convert integer 45 into float
num = 45
f = float(num)
print(f)
# 11. Convert number 100 into string
num = 100
s = str(num)
print(s)
# 12. Find the average of five numbers
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
n5 = float(input("Enter fifth number: "))

average = (n1 + n2 + n3 + n4 + n5) / 5
print("Average =", average)
# 13. Calculate the perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = 2 * (length + width)
print("Perimeter =", perimeter)
# 14. Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit =", fahrenheit)
# 15. Convert kilometers into meters
km = float(input("Enter kilometers: "))
meters = km * 1000
print("Meters =", meters)
# 16. Display full name in uppercase
name = input("Enter your full name: ")
print(name.upper())
# 17. Display the first character of a word
word = input("Enter a word: ")
print(word[0])
# 18. Display the last character of a word
word = input("Enter a word: ")
print(word[-1])
# 19. Join two strings
str1 = "Python"
str2 = "Programming"

sentence = str1 + " " + str2
print(sentence)
# 20. Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    # 22. Assign grades
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")
# 23. Check vowel or consonant
ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")
# 24. Print the pattern using a while loop

i = 1

while i <= 5:
    print(str(i) * i)
    i += 1
# 25. Function to count vowels

def count_vowels(word):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in word:
        if ch in vowels:
            count += 1

    return count

word = input("Enter a word: ")
print("Number of vowels =", count_vowels(word))
for i in range(5):
    print("*")
for i in range(10):
    print("#")
for i in range(10):
    print("*", end="")
for i in range(20):
    print("=", end="")
for i in range(5):
    print("😊", end="")
for i in range(1, 11):
    print(i, end=" ") 
for i in range(1, 6):
    print("#" * i)
for i in range(1, 6):
    print("@" * i)
for i in range(1, 6):
    print("$" * i)
for i in range(5, 0, -1):
    print("*" * i)
for i in range(1, 6):
    print(str(i) * i)
letters = ["A", "B", "C", "D", "E"]

for i in range(5):
    print(letters[i] * (i + 1))
for i in range(1, 6):
    print("😊" * i)
for i in range(5):
    print("*" * 5)
for i in range(4):
    print("#" * 8)
for i in range(1, 6):
    print(str(i) * 5)
for i in range(1, 6):
    for j in range(i, i + 5):
        print(j, end="")
    print()
for i in range(5):
    if i == 0 or i == 4:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")
    for i in range(4):
        i == 0 or i == 3
        print("#" * 8)
    else:
        print("#" + " " * 6 + "#")
    for i in range(1, 6):
        print(" " * (5 - i) + "*" * (2 * i - 1))
    for i in range(5, 0, -1):
        print(" " * (5 - i) + "*" * (2 * i - 1))
    for i in range(1, 6):
        print(" " * (5 - i) + "*" * (2 * i - 1))

for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
print("   *")
print("  ***")
print(" *****")
print("*******")
print("*     *")
print("* []  *")
print("*_____*")
print("    *")
print("   ***")
print("  *****")
print(" *******")
print("*********")
print("   ***")
print("   ***")
print(" **   ** ")
print("**** ****")
print(" ********")
print("  ******")
print("   ****")
print("    **")
print(" *****")
print("*")
print("*")
print("*")
print(" *****")
for i in range(5):
    for j in range(6):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("O", end="")
    print()
for i in range(1, 6):
    print("#" * i)

for i in range(4, 0, -1):
    print("#" * i)
    
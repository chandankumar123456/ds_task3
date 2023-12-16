print("Day-3")

input("Enter a number : ")
#but it doesn't store it Therefore we use a variable to store it
num = input("Enter a number :")
print(type(num))
#the entered number is string type so we need to type cast it for integer

num = int(input("Enter a number : "))
print(num)
print(type(num))

name = input("Enter your name : ")
print("Hello, Welcome to course :", name)

fnum = float(input("Enter a float number : "))
print(fnum)

list1 = ["Chandan", "Kumar", "ChandanKumar", "Hello"]
print(list1[2])
print(len(list1))
list1.append("World!")
#to use pop we give index number but if we want to remove using name we use remove method
list1.pop(1)
list1.remove("Hello")
list1.insert(0, "23")
list1[0] = "2329"
print(list1)

print("Tuple and it's operation : ")
t = (1, 2, 3, 4, 5)
print(t)

print("Adding value into tuple by type casting it into list : ")
t = (1, 2, 3, 4, 5)
print(t)
temp = list(t)
temp.append(6)
t = temp
t = tuple(t)
print(t)

"""
Another way:
t = (1, 2, 3, 4, 5)
t = tuple(list(t) + [6])
print(t)
t = (1, 2, 3, 4, 5)
t = tuple(list(t) + [6])
print(t)
"""
print("Using import/pip : ")
import math
pi_val = math.pi
print("The vallue of pi is : ", pi_val)
num = int(input("Enter a number : "))
ans = math.sqrt(num)
print(f"The square root of {num} is {ans}")

floor_val = math.floor(23.9)
ceil_val = math.ceil(22.9)
print(f"floor value  of 23.9 is {floor_val} and ceil value 22.9 is {ceil_val}")

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
print(arr)
# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("Hello user, this is a python program for letter counter")
s=input("Enter the string:")
let=input("Enter the letter to be searched:")
count=s.count(let)
print(count)
n=len(s)
per=(count*100)/n
print("percentage is",per)
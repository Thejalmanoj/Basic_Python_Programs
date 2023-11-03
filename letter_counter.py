print("Hello user, this is a python program for letter counter")
s=input("Enter the string:")
let=input("Enter the letter to be searched:")
count=s.count(let)
print(count)
n=len(s)
per=(count*100)/n
print("percentage is",per)

# Complete this program to classify people by age


# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

age = int(input("enter age:"))
print(" enter age: " ,age)
if age >= 0 and age <=12:
    print ("child")
elif age >= 13 and  age <= 19 :
    prnit("teenager")
elif age >= 20 and age <=59:
    print("adult")
else:
    print("senior")

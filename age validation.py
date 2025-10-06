age = int(input("What is your age? " ))
while age < 0 or age > 130:
    print("Your age is wrong")
    age = int(input("What is your age? " ))
    break
print("You entered correct age")





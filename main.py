print("""What math operation would you like to perform?
add
subtract
multiply
divide""")
m = input()
if m == "add":
    print("What two numbers would you like to add:")
    print("First number:")
    x = input()
    print("Second number:")
    y = input()
    z = float(x) + float(y)
    txt = "Your solution is {}."
    print(txt.format(z))
elif m == "subtract":
    print("What two numbers would you like to subtract:")
    print("First number:")
    x = input()
    print("Second number:")
    y = input()
    z = float(x) - float(y)
    txt = "Your solution is {}."
    print(txt.format(z))
elif m == "multiply":
    print("What two numbers would you like to multiply:")
    print("First number:")
    x = input()
    print("Second number:")
    y = input()
    z = float(x) * float(y)
    txt = "Your solution is {}."
    print(txt.format(z))
elif m == "divide":
    print("What two numbers would you like to divide:")
    print("First number:")
    x = input()
    print("Second number:")
    y = input()
    z = float(x) / float(y)
    txt = "Your solution is {}."
    print(txt.format(z))
else:
    print("""I do not understand. Please start over and choose one from the following list:
    add
    subtract
    multiply
    divide""")

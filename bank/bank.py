greeting = input("Greeting: ")
greeting = greeting.lower()
print(greeting[0:5])

if greeting[0:5] == "hello":
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")

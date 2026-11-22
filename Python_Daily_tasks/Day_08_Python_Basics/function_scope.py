message = "I am a global variable"
def display():
    name = "Arikaran"
    print("Local variable:", name)
    print("Global variable:", message)
display()
print("Outside function:", message)

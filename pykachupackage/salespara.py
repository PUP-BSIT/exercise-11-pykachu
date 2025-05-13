import pyjokes

def give_joke():
    name = input("Enter your name: ")
    joke = pyjokes.get_joke()

    print(f"\nHello, {name}!")
    print(f"Here's a joke for you: ")
    print(f"\n {joke}")
    print (f"\nI hope it made you giggle, {name}! <3 \n")
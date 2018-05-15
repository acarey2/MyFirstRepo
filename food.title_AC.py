def hello(name):
    print("Hello" + name + "!")
    print("How's it going?")
    day = input("Is your day looking good?")
    day = day.title()
    if day == "Yes":
        print("That's great!")

    elif day == ("No"):
        print ("I'm sorry to hear that!")

    else:
        print("I didn't quite catch that.")

while True:
    food = input ("What's for lunch today?")
    food = food.lower()
    if food == " chicken nuggets":
        print("bleh, but correct")
        break
    elif food == " pizza":
        print ("yay")
    else:
        print ("cool")

    print ("ok bye")
        

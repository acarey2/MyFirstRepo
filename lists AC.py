name= " annie"
subjects = [" english", " math", " history"," spanish", " science"]

print ("Hello" + name)
for i in subjects:
    print ("One of my subjects is" + i)

shows = [" gossip girl", " friends", " riverdale", "90210", " the good place", " the 100", "stranger things", "pretty little liars"]
for i in shows:
    if i == " gossip girl":
        print (i + " is a great show to watch when your in the mood for some highschool mystery or romance")
    elif i == " friends" or i == " the good place":
        print (i + " is a great show to watch when you want to feel happpppy :)")
    else:
        print (i + " is a great show if you want some mystery or to be scared")

tvshow= []
while True:
    print ("What's one of your favorite tvshow. Type 'end' to stop.")
    answer = input()
    if answer == "end":
        break
    else:
        tvshow.append(answer)

for i in tvshow:
    print ("one of your favorite tv shows is " + i)
    

    
        

import pyautogui as pg
import time
import webbrowser
# sets points to zero at start
#1= style= casual/comfy
#2= style= classic/chic
#3= style= girly/preppy
#4= style= adventurous/bold

points=0




#Questions for player
webbrowser.open ("https://drive.google.com/file/d/1kmWkWozdblS41o5Q2IKlhHhs3y-fkyN_/view?usp=sharing")
answer= pg.prompt("""
how adventurous is your style?
one 
two
three
four
five
""")
# tells player their choice


#gives points based on choice
if answer == "one":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "two":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "three":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "four":
    pg.alert("You gain 5 points")
    points += 5
elif answer == "five":
    pg.alert("You gain 5 points")
    points += 5

    answer= pg.prompt ("""
which word best describes your style?
a) chic and laid-back
b) bold,out-there
c) girly and pretty
d) smart and clean

""")
# tells player their choice
#gives points based on choice
if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 5 points")
    points += 5
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3
elif answer == "d":
    pg.alert("You gain 2 points")
    points += 2


answer= pg.prompt ("""
How much do you like shopping
a) love it!
b) I'll shop for like an hour
c) only online shopping
d) I hate shopping

""")
# tells player their choice
#gives points based on choice

if answer == "a":
    pg.alert("You gain 5 points")
    points += 5
elif answer == "b":
    pg.alert("You gain 4 point")
    points += 4
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3
elif answer == "d":
    pg.alert("You gain 1 point")
    points += 1
webbrowser.open ("https://drive.google.com/file/d/10Wdo9CGecP8zi78dBbwvFsk5XVaUglw-/view?usp=sharing")
answer= pg.prompt ("""
Which weekday style?
one
two
three
four
five
six
""")
# tells player their choice
#gives points based on choice

if answer == "one":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "two":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "three":
    pg.alert("You gain 4 points")
    points += 4
elif answer == "four":
    pg.alert("You gain 5 points")
    points += 5
elif answer == "five":
    pg.alert("You gain 7 points")
    points += 7
elif answer == "six":
    pg.alert("You gain 5 poinst")
    points += 5
webbrowser.open ("https://drive.google.com/file/d/1jn1ujdAeTUDajgszGoAdDb4Hhl-ponkc/view?usp=sharing")
answer= pg.prompt ("""
Which weekend style?
one
two
three
four
five
six
""")
# tells player their choice
#gives points based on choice

if answer == "one":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "two":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "three":
    pg.alert("You gain 5 points")
    points += 5
elif answer == "four":
    pg.alert("You gain 4 points")
    points += 4
elif answer == "five":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "six":
    pg.alert("You gain 3 points")
    points += 3
webbrowser.open("https://drive.google.com/file/d/1MWeuYUmHdqzognMnpvCJ78vsowqX2I-m/view?usp=sharing")
answer= pg.prompt ("""
Which party outfit?
one
two
three
four
five
six
""")
# tells player their choice
#gives points based on choice
if answer == "one":
    pg.alert("You gain 2 points")
    points += 2
elif answer == "two":
    pg.alert("You gain 3 points")
    points += 3
elif answer == "three":
    pg.alert("You gain 3 points")
    points += 3
elif answer == "four":
    pg.alert("You gain 4 points")
    points += 4
elif answer == "five":
    pg.alert("You gain 7 points")
    points += 7
elif answer == "six":
    pg.alert("You gain 5 points")
    points += 5

#END OF SURVEY
pg.alert("You got a total of "+ str(points)+ "points")
if points <=10 and points >=5:
    webbrowser.open ("https://i.pinimg.com/originals/15/55/02/155502632fc62d06d5cf8e9570c9fc95.jpg")
    pg.alert("Your fashion sense is laid- back, and casual")
if points <=20 and points >=10:
     webbrowser.open ("http://thezoereport.com/wp-content/uploads/2016/08/800x800-Recovered-2-600x600.jpg")
     pg.alert("Your fashion sense is minimal, smart, and polished")
if points <=30 and points >=20:
    webbrowser.open ("https://cdn.cliqueinc.com/posts/img/uploads/current/images/0/63/74/main.original.640x0c.jpg")
    pg.alert("Your fashion sense is pretty, feminine, and glam ")
if points >=30:
    webbrowser.open ("http://www.sydnestyle.com/wp-content/uploads/2016/02/Sydne-Style-wears-a-Nicole-Miller-grafitti-print-skirt-from-new-york-fashion-week-runway.jpg")
    pg.alert("Your fashion sense is bold, edgy, adventurous, and makes a statement")
     










     
                   

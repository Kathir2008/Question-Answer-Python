Score = 0 
player = input("If you play the game: ")

if player.lower() == "yes" :
    print("Okay Start Now the Game")
    question1 = input("The XML is the Markup language (y/n) : ")
    if question1 == "y":
        Score += 1
        print("Super")
    else :
        print("Sorry,Wrong Anwser Try Next time")

    question2 = input("The Python is used to bulid Wordpress site (y/n) : ")
    if question2 == "n":
        Score += 1
        print("Super")
    else :
        print("Sorry,Wrong Anwser Try Next time")

    question3 = input("PHP is a server side scripting language  (y/n) : ")
    if question3 == "y":
        Score += 1
        print("Super")

    print("Super Your Score is " + str(Score))
else:
    quit()
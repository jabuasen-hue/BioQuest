import time

difficultyMenu = ("-------------------------------------"
                  "| 1. Easy                           |"
                  "| 2. Medium                         |"
                  "| 3. Hard                           |"
                  "-------------------------------------")


def mainMenu():
    while True:
        print("=======================================")
        time.sleep(0.25)
        print("||             MAIN MENU             ||")
        time.sleep(0.25)
        print("---------------------------------------")
        time.sleep(0.25)
        print("| 1. Play                             |")
        time.sleep(0.25)
        print("| 2. Instructions                     |")
        time.sleep(0.25)
        print("| 3. Achievements                     |")
        time.sleep(0.25)
        print("| 4. Credits                          |")
        time.sleep(0.25)
        print("| 5. Quit                             |")
        time.sleep(0.25)
        print("---------------------------------------")
        time.sleep(1)
        menuChoice = input("| What would you like to do? (1-4): ")
        while menuChoice not in ["1", "2", "3", "4"]:
            print("\n Please Enter a valid answer \n")
            break

        if menuChoice == "1":
            playOption()
        elif menuChoice == "2":
            instructionsOption()
        elif menuChoice == "3":
            achievementsOption()
        elif menuChoice == "4":
            creditsOption()
        else:
            break


def playOption():
    while True:
        time.sleep(2)
        print("\n =============== PLAY ==============")
        time.sleep(0.25)
        print("-------------------------------------")
        time.sleep(0.25)
        print("| 1. Identification                 |")
        time.sleep(0.25)
        print("| 2. Multiple Choice                |")
        time.sleep(0.25)
        print("-------------------------------------")
        time.sleep(1)
        quizChoice = input("| What quiz type do you want? (1 or 2): ")
        while quizChoice not in ["1", "2"]:
            print("\n Please Enter a valid answer \n")
            break
    
        if quizChoice == "1":                          
            print("")               
        else:
            print("")

        print("-------------------------------------")
        print("| Quarter Options:                  |")
        print("| 1. First Quarter                  |")
        print("| 2. Second Quarter                 |")
        print("| 3. Third Quarter                  |")
        print("| 4. Fourth Quarter                 |")
        print("-------------------------------------")
        quarterChoice = input("| What quarter would you like to study? (1-4): ")
        while quarterChoice not in ["1", "2", "3", "4"]:
            print("\n Please Enter a valid answer \n")
            break
    
        if quarterChoice == "1":                          
            print("")               
        elif quarterChoice == "2":
            print("")
        elif quarterChoice == "3":
            print("")
        else:
            print("")



def instructionsOption():
    print("\n ============= INSTRUCTIONS ============")
    print("BioQuest is a program that aims to make Biology fun ! Whether homework, reviews, or big tests, BioQuest is here to help!")
    print("\nHow To Play:")
    print("1. Choose Your Tutor Pick a tutor persona that matches your learning style.")
    print("2. Select Your Topics Choose from any topic covered during the quarter. Everything—from cells to genetics—appears as a ready-made quiz list.")
    print("3. Pick a Quiz Mode Different quiz types make learning flexible and fun: Multiple Choice or Identification")
    print("4. Answer and Explore Take the quiz at your own pace. Tutors will guide you with hints, explanations, and encouragement.")
    print("5. Track Your Progress! Your results are saved day by day and automatically transferred to Google Sheets, so you can monitor improvements over time.")
    print("\nEach option on the menu will lead you somewhere, just like how it led you here!")
    print("Play - Choose this option to begin your quest and start playing!")
    print("Achievements - Choose this option to look at everything you have accomplished so far.")
    print("Credits - Choose this option to look at the people who have contributed to the making of this program.")
    print("Quit - Choose this option to exit the program.\n")

def achievementsOption():
    print("Uh oh! That isn't available yet! This will be added soon :D")
    
def creditsOption():
    print("\n =============== CREDITS ===============")
    print("      Program     ")
    print(" Conceptualized By: Buasen, Julian Jesse")
    print("                    Sanoy, Jeraiza Leigh")
    print("                    Sagario, Julien Alexa")
    print("                      (Honorary Mention) ")
    print("\n Program Created By: Buasen, Julian Jesse")
    print("                     Sanoy, Jeraiza Leigh")
    print("\n Grade & Section: 8 - Sampaguita")
    print(" Subject: Computer Science")
    print(" Teacher: Ma'am Kaye Alamag")
    print("\n - Thank you for using this program! <3 - \n")
    
    
mainMenu()

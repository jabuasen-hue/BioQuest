quizMenu = ("\n================ QUIZ ==============="
    "\n-------------------------------------"
    "\n| 1. Identification                 |"
    "\n| 2. Multiple Choice                |"
    "\n-------------------------------------")
    
difficultyMenu = ("\n============= DIFFICULTY ============"
    "-------------------------------------"
    "| 1. Easy                           |"
    "| 2. Medium                         |"
    "| 3. Hard                           |"
    "-------------------------------------")

def mainMenu():
    while True:
        print("=======================================")
        print("||             MAIN MENU             ||")
        print("---------------------------------------")
        print("| 1. Play                             |")
        print("| 2. Instructions                     |")
        print("| 3. Achievements                     |")
        print("| 4. Credits                          |")
        print("| 5. Quit                             |")
        print("---------------------------------------")
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
        print("\n =============== PLAY ==============")
        print("-------------------------------------")
        print("| 1. Georgina                       |")
        print("| 2. Julien                         |")
        print("-------------------------------------")
        quizChoice = input("| Who will be your tutor for today? (1 or 2): ")
        while tutorChoice not in ["1", "2"]:
            print("\n Please Enter a valid answer \n")
            break
    
            if tutorChoice == "1":                          
                print("")               
            else:
                print("")
                
        print("-------------------------------------")
        print("| 1. Identification                 |")
        print("| 2. Multiple Choice                |")
        print("-------------------------------------")
        quizChoice = input("| What quiz type do you want? (1 or 2): ")
        while quizChoice not in ["1", "2"]:
            print("\n Please Enter a valid answer \n")
            break
    
        if quizChoice == "1":                          
            print("")               
        else:
            print("")


def instructionsOption():
    print("\n ============= INSTRUCTIONS ============")
    print("BioQuest is a program that aims to make Biology fun ! ...")

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

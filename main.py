quizMenu = ("\n================ QUIZ ==============="
    "\n-------------------------------------"
    "\n| 1. Identification                 |"
    "\n| 2. True or False                  |"
    "\n| 3. True or False (Modified)       |"
    "\n| 4. Multiple Choice                |"
    "\n-------------------------------------")
    
difficultyMenu = ("\n============= DIFFICULTY ============"
    "\n-------------------------------------"
    "\n| 1. Easy                           |"
    "\n| 2. Medium                         |"
    "\n| 3. Hard                           |"
    "\n| 2. Difficult                      |"
    "\n-------------------------------------")

def mainMenu():
    while True:
        print("=======================================")
        print("||             MAIN MENU             ||")
        print("---------------------------------------")
        print("| 1. Play                             |")
        print("| 2. Achievements                     |")
        print("| 3. Credits                          |")
        print("| 4. Quit                             |")
        print("---------------------------------------")
        menuChoice = input("| What would you like to do? (1-4): ")
        while menuChoice not in ["1", "2", "3", "4"]:
            print("\n Please Enter a valid answer \n")
            break
        
        if menuChoice == "1":
            playOption()
        elif menuChoice == "2":
            achievementsOption()
        elif menuChoice == "3":
            creditsOption()
        else:
            break
    
def playOption():
    while True:
        print("\n =============== PLAY ==============")
        print("|               TOPICS              |")
        print("-------------------------------------")
        print("| 1. First Quarter                  |")
        print("| 2. Second Quarter                 |")
        print("| 3. Third Quarter                  |")
        print("| 4. Fourth Quarter                 |")
        print("-------------------------------------")
        quarterChoice = input("| Which quarter will you study/review? (1-4): ")
        while quarterChoice not in ["1", "2", "3", "4"]:
            print("\n Please Enter a valid answer \n")
            break
    
        if quarterChoice == "1" or "2" or "3" or "4":                          
            print("Uh oh! That isn't available yet! This will be added soon :D")
            break               
        
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

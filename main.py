import time
import json

try:
    # READING from the file
    filename = "easyQuestionsMP.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        easyMP = json.load(file)

    filename = "mediumQuestionsMP.json"
    with open(filename, 'r') as file:
        medMP = json.load(file)

    filename = "hardQuestionsMP.json"
    with open(filename, 'r') as file:
        hardMP = json.load(file)


    def diffMenu():
        print(" " * 92, "\n-------------------------------------")
        time.sleep(0.25)
        print(" " * 92, "| Difficulty Options:               |")
        time.sleep(0.25)
        print(" " * 92, "| 1. Easy                           |")
        time.sleep(0.25)
        print(" " * 92, "| 2. Medium                         |")
        time.sleep(0.25)
        print(" " * 92, "| 3. Hard                           |")
        time.sleep(0.25)
        print(" " * 92, "-------------------------------------")
        time.sleep(1)
        diffChoice = input("| What difficulty would you like to answer? (1-3): \n").strip()
        return diffChoice


    def quarterMenu():
        print(" " * 92, "\n-------------------------------------")
        time.sleep(0.25)
        print(" " * 92, "| Quarter Options:                  |")
        time.sleep(0.25)
        print(" " * 92, "| 1. First Quarter                  |")
        time.sleep(0.25)
        print(" " * 92, "| 2. Second Quarter                 |")
        time.sleep(0.25)
        print(" " * 92, "| 3. Third Quarter                  |")
        time.sleep(0.25)
        print(" " * 92, "| 4. Fourth Quarter                 |")
        time.sleep(0.25)
        print(" " * 92, "-------------------------------------")
        time.sleep(1)
        quarterChoice = int(input("| What quarter would you like to study? (1-4): ").strip())
        return quarterChoice


    def mainMenu():
        while True:
            print(" " * 91, "=======================================")
            time.sleep(0.25)
            print(" " * 91, "||             MAIN MENU             ||")
            time.sleep(0.25)
            print(" " * 91, "---------------------------------------")
            time.sleep(0.25)
            print(" " * 91, "| 1. Play                             |")
            time.sleep(0.25)
            print(" " * 91, "| 2. Instructions                     |")
            time.sleep(0.25)
            print(" " * 91, "| 3. Achievements                     |")
            time.sleep(0.25)
            print(" " * 91, "| 4. Credits                          |")
            time.sleep(0.25)
            print(" " * 91, "| 5. Quit                             |")
            time.sleep(0.25)
            print(" " * 91, "---------------------------------------")
            time.sleep(1)
            menuChoice = input("| What would you like to do? (1-4): ").strip()
            while menuChoice not in ["1", "2", "3", "4"]:
                menuChoice = input("\n Please Enter a valid answer \n").strip()


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
            print(" " * 92, "\n =============== PLAY ==============")
            time.sleep(0.25)
            print(" " * 92, "-------------------------------------")
            time.sleep(0.25)
            print(" " * 92, "| 1. Identification                 |")
            time.sleep(0.25)
            print(" " * 92, "| 2. Multiple Choice                |")
            time.sleep(0.25)
            print(" " * 92, "-------------------------------------")
            time.sleep(1)
            quizChoice = input("| What quiz type do you want? (1 or 2): ").strip()
            while quizChoice not in ["1", "2"]:
                quizChoice = input("\n Please Enter a valid answer \n").strip()

            if quizChoice == "1":
                quarterOptionIdentif()
            else:
                quarterOptionMultiple()


    def quarterOptionIdentif():
        quarterChoice = quarterMenu()
        while quarterChoice not in ["1", "2", "3", "4"]:
            quarterChoice = input("\n Please Enter a valid answer \n").strip()

        if quarterChoice == "1":
            print("")
        elif quarterChoice == "2":
            print("")
        elif quarterChoice == "3":
            print("")
        else:
            print("")

        diffChoice = diffMenu()


    def quarterOptionMultiple():
        quarterChoice = quarterMenu()
        while quarterChoice not in [1, 2, 3, 4]:
            quarterChoice = input("| Please Enter a valid answer: \n").strip()

        if quarterChoice == 1:
            print("")
        elif quarterChoice == 2:
            print("")
        elif quarterChoice == 3:
            print("")
        else:
            print("")

        diffChoice = diffMenu()
        if diffChoice == "1":
            questions = easyMP
        elif diffChoice == "2":
            questions = medMP
        else:
            questions = hardMP
            
        for q in questions:
            if q["quarter"] == quarterChoice:
                a = input(q["question"]).upper().strip()
                time.sleep(0.5)
                if a == q["answer"]:
                    print("joosy")
                else:
                    print("aww")
                    time.sleep(1)
                print(q["explanation"])
                time.sleep(1.5)
                input("\nPress Enter to proceed to next question")

    def instructionsOption():
        print("\n ============= INSTRUCTIONS ============")
        print(
            "BioQuest is a program that aims to make Biology fun ! Whether homework, reviews, or big tests, BioQuest is here to help!")
        print("\nHow To Play:")
        print("1. Choose Your Tutor Pick a tutor persona that matches your learning style.")
        print(
            "2. Select Your Topics Choose from any topic covered during the quarter. Everything—from cells to genetics—appears as a ready-made quiz list.")
        print("3. Pick a Quiz Mode Different quiz types make learning flexible and fun: Multiple Choice or Identification")
        print(
            "4. Answer and Explore Take the quiz at your own pace. Tutors will guide you with hints, explanations, and encouragement.")
        print(
            "5. Track Your Progress! Your results are saved day by day and automatically transferred to Google Sheets, so you can monitor improvements over time.")
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

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

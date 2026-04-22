import time
import json

try:
    # READING from the file
    with open("easyQuestionsMP.json", 'r', encoding="utf-8") as file:
        # Load the JSON data from the file
        easyMP = json.load(file)

    with open("hardQuestionsMP.json", 'r', encoding="utf-8") as file:
        hardMP = json.load(file)

    with open("easyID.json", 'r', encoding="utf-8") as file:
        easyID = json.load(file)

    with open("hardID.json", 'r', encoding="utf-8") as file:
        hardID = json.load(file)


    def diffMenu():
        print(" " * 92, "-------------------------------------")
        time.sleep(0.25)
        print(" " * 92, "| Difficulty Options:               |")
        time.sleep(0.25)
        print(" " * 92, "| 1. Easy                           |")
        time.sleep(0.25)
        print(" " * 92, "| 2. Hard                           |")
        time.sleep(0.25)
        print(" " * 92, "-------------------------------------")
        time.sleep(1)
        diffChoice = input("| What difficulty would you like to answer? (1 or 2): ").strip()
        return diffChoice


    def quarterMenu():
        print(" " * 92, "-------------------------------------")
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
            menuChoice = input("| What would you like to do? (1-5): ").strip()
            while menuChoice not in ["1", "2", "3", "4", "5"]:
                menuChoice = input("\n Please Enter a valid answer: ").strip()
            for x in range(100):
                print()


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
            time.sleep(1)
            print()
            print(" " * 92, "================ PLAY ===============")
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
                quizChoice = input("\n Please Enter a valid answer ").strip()

            if quizChoice == "1":
                quarterOptionIdentif()
            else:
                quarterOptionMultiple()


    def quarterOptionIdentif():
        quarterChoice = quarterMenu()
        while quarterChoice not in ["1", "2", "3", "4"]:
            quarterChoice = input("\n Please Enter a valid answer ").strip()

        if quarterChoice == "1":
            print("")
        elif quarterChoice == "2":
            print("")
        elif quarterChoice == "3":
            print("")
        else:
            print("")

        diffChoice = diffMenu()
        if diffChoice == "1":
            questions = easyID
        else:
            questions = hardID

        for q in questions:
            if q["quarter"] == quarterChoice:
                print()
                print("-" * 221 + "\n")
                print(f" | {q['question']}")
                time.sleep(0.5)
                print(f" | {q['options']}")
                time.sleep(0.5)

                a = input(" | What is your answer?: ").strip().capitalize()

                if a == q["answer"]:
                    print(" | Correct!")
                else:
                    print(" | Incorrect...")
                    print(f" | The correct answer is: {q['answer']}!")

                time.sleep(1.5)
                input("\n | Press Enter to proceed to next question")

    def quarterOptionMultiple():
        quarterChoice = quarterMenu()
        while quarterChoice not in [1, 2, 3, 4]:
            quarterChoice = input("| Please Enter a valid answer: ").strip()

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
        else:
            questions = hardMP
            
        for q in questions:
            if q["quarter"] == quarterChoice:
                print()
                print("-" * 221 + "\n")
                print("\n", " " * 90, " ------------- Question  -------------")
                print(f" | {q['question']}")
                time.sleep(0.5)
                print(f" | {q['options']}")
                time.sleep(0.5)

                a = input(" | What is your answer?: ").strip().capitalize()

                if a == q["answer"]:
                    print(" | Correct!")
                else:
                    print(" | Incorrect...")
                    print(f" | The correct answer is: {q['answer']}!")

                time.sleep(1.5)
                input("\n | Press Enter to proceed to next question")

    def instructionsOption():
        print("\n", " " * 90, " ============= INSTRUCTIONS ============")
        print(" | BioQuest is a program that aims to make Biology fun! Whether homework, reviews, or big tests, BioQuest is here to help!")
        print("\n | How To Play:")
        print(" |  1. Choose Your Tutor. Pick a tutor persona that matches your learning style.")
        print(" |  2. Select Your Topics. Choose from any topic covered during the quarter. Everything—from cells to genetics—appears as a ready-made quiz list.")
        print(" |  3. Pick a Quiz Mode. Different quiz types make learning flexible and fun: Multiple Choice or Identification")
        print(" |  4. Answer and Explore. Take the quiz at your own pace. Tutors will guide you with hints, explanations, and encouragement.")
        print(" |  5. Track Your Progress! Your results are saved day by day and automatically transferred to Google Sheets, so you can monitor improvements over time.")
        print("\n | Each option on the menu will lead you somewhere, just like how it led you here!")
        print(" |  Play - Choose this option to begin your quest and start playing!")
        print(" |  Achievements - Choose this option to look at everything you have accomplished so far.")
        print(" |  Credits - Choose this option to look at the people who have contributed to the making of this program.")
        print(" |  Quit - Choose this option to exit the program.\n")

        input("Press ENTER to continue")

        print("\n" + "-" * 221, "\n")


    def achievementsOption():
        print("\n", " " * 90, " ============= ACHIEVEMENTS ============")
        print(" | Uh oh! That isn't available yet! This will be added soon :D")

        input(" | Press ENTER to continue")

        print("\n" + "-" * 221, "\n")


    def creditsOption():
        print("\n", " " * 89, " =============== CREDITS ===============")
        print(" |      Program     ")
        print(" | Conceptualized By: Buasen, Julian Jesse")
        print(" |                    Sanoy, Jeraiza Leigh")
        print(" |                    Sagario, Julien Alexa")
        print(" |                      (Honorary Mention) ")
        print("\n | Program Created By: Buasen, Julian Jesse")
        print(" |                     Sanoy, Jeraiza Leigh")
        print("\n | Grade & Section: 8 - Sampaguita")
        print(" | Subject: Computer Science")
        print(" | Teacher: Ma'am Kaye Alamag")
        print("\n | - Thank you for using this program! <3 - \n")

        input("Press ENTER to continue")

        print("\n" + "-" * 221, "\n")

    mainMenu()

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

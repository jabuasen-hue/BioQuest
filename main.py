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
        quarterChoice = input("| What quarter would you like to study? (1-4): ").strip()
        return quarterChoice


    def mainMenu():
        while True:
            print("=" * 72, "BIOQUEST", "=" * 72)
            # Welcome Statement
            time.sleep(3)
            print(" | Hi! and welcome to...")
            time.sleep(3)
            print("                                                           _____  _        ___                  _   ")
            print("                                                          | ___ )(_) ___  / _ \ _   _  ___  ___| |_ ")
            print("                                                          |  _  \| |/ _ \| | | | | | |/ _ \/ __| __|")
            print("                                                          | |_) || | (_) | |_| | |_| |  __/\__ \ |_ ")
            print("                                                          |_____/|_|\___/ \__\_\__,__|\___||___/\__|")
            time.sleep(2)
            print("\n | This is a quizzer, wherein you try your best to answer a series of questions correctly.")
            time.sleep(2)
            print(" | Make sure to have fun!")
            time.sleep(2)
            print(" | Try to explore more before trying out the main game")
            time.sleep(2)
            print(" | Anyways, enjoy!")
            time.sleep(1)
            print("\n                                                ", "=" * 65)
            time.sleep(0.25)
            print("                                                 ||  __  __    __    ____  _  _    __  __  ____  _  _  __  __   ||")
            time.sleep(0.25)
            print("                                                 || '  '`  )  ,__`  (_  _)( `( )  (  '`  )| ___)( `( )( |  | )  ||")
            time.sleep(0.25)
            print("                                                 || |      | ,(__)`  _||_ |    |  |      ||__)  |  ` || |__| |  ||")
            time.sleep(0.25)
            print("                                                 || (_)||(_)(__)(__)(____)(_)`_)  (_)||(_)|____)(_)`_)(______)  ||")
            time.sleep(1)
            print("                                                 ||-------------------------------------------------------------||")
            time.sleep(0.25)
            print("                                                 ||1. Start Game                                                ||")
            time.sleep(0.25)
            print("                                                 ||2. Instructions                                              ||")
            time.sleep(0.25)
            print("                                                 ||3. Achievements                                              ||")
            time.sleep(0.25)
            print("                                                 ||4. Credits                                                   ||")
            time.sleep(0.25)
            print("                                                 ||5. Quit                                                      ||")
            print("                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
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
            time.sleep(1)
            print(" | System: Hi there...")
            time.sleep(0.5)
            print("\n | System: Sorry, may I ask what I should call you by?")
            time.sleep(0.5)
            name = input(" | Enter your nickname: ")
            time.sleep(1)
            print(f"\n | System: Nice name, {name}!")
            time.sleep(0.5)
            print(" | System: Now, please choose your tutor:")
            time.sleep(5)
            tutor = input(" | Who do you prefer?: ")
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

        runQuiz(questions)

    def quarterOptionMultiple():
        quarterChoice = quarterMenu()
        while quarterChoice not in ["1", "2", "3", "4"]:
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

        runQuiz(questions)

# ===================================================================================================================
# Run Quiz
    def runQuiz(questions):
        for q in questions:
            cont = "Y"
            gameEnd = "======================================================================== GAME END ========================================================================"

            if cont == "Y":  # Checks if player chose to continue
                askedIndices = 0
                score = 0

                print(" " * 67, "----------------")  # Border
                print(" " * 67, "|Starting Round|")
                print(" " * 67, "----------------")  # Border

                while askedIndices < 5:  # Will check if the maximum amount of questions have already been asked
                    # Tells player what question they are on
                    time.sleep(1.5)
                    print("\n" + " " * 60, "=" * 30)
                    print(" " * 60, f"=           {askedIndices + 1} of 5           =")
                    print(" " * 60, "=" * 30)

                    # Displays question
                    time.sleep(1.5)
                    print("-" * 100)
                    print(q["question"])
                    print("-" * 100)
                    time.sleep(1.5)
                    print(q["options"])

                    # Input Validation
                    print("=" * 36)
                    userAnswer = input(">>> Please enter your answer (A/B/C/D): ").upper().strip()
                    print("=" * 36)
                    while userAnswer not in ["A", "B", "C", "D"]:
                        userAnswer = input(">>> Invalid answer. Please enter A, B, C, or D: ").upper().strip()

                    # Checks if users answer is correct or not
                    if userAnswer == q["answer"]:
                        print("\n" + "*" * 50)
                        print(" " * 21, "Correct!")
                        print("*" * 50, "\n")
                        score += 1 # Updates user score
                        print("You have earned a point!")
                    else:
                        print("\n" + "*" * 50)
                        print(" " * 20, "Incorrect")
                        print("*" * 50, "\n")
                    time.sleep(1)
                    print("\n>>> Answer: ", q["answer"])
                    time.sleep(2)
                    print(">>> Explanation: ", q["explanation"], "\n")  # Displays an explanation regardless if player is right or wrong
                    askedIndices += 1 # Adds one to the variable to show one question has already been answered

                    # Asks player if they want to continue
                    if askedIndices < 5:  # Checks if the amount of asked questions is lesser than questions per era
                        print("=" * 33)
                        cont = input("|Do you want to continue? (Y/N): ").upper().strip()
                        print("=" * 33)
                        while cont not in ["Y", "N"]:  # Input Validation
                            cont = input("Invalid input. Do you want to continue? (Y/N): ").upper().strip()
                        if cont == "N":  # If player chose to not continue
                            print("Thanks for playing! Returning to main menu...")
                            time.sleep(1.5)
                            print(gameEnd, "\n")
                            break  # Terminates loop
                        else:
                            continue  # Stops the while loop but continues the for loop

                    # Outcome of round
                    if askedIndices == 5:
                        print("\n" + "-" * 150)  # Border
                        time.sleep(1.5)
                        print(f"You've completed this difficulty!")
                        time.sleep(1.5)
                        print(f"Your score is {score} out of 5")  # Displays score
                        time.sleep(1.5)
                        input("Press Enter to go to menu")  # Provides a brief period of time for players to read/reflect

            else:
                break  # Terminates loop and ends game

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

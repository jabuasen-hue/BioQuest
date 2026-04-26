import time
import random
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

    with open("dialogue.json", 'r', encoding="utf-8") as file:
        dialogue = json.load(file)


    def tutorSelection():
        refusalCount = 0
        time.sleep(1)
        print(" | System: Hi there...")
        time.sleep(1)
        print(" | System: Sorry, may I ask what I should call you by?")
        time.sleep(0.5)
        name = input(" | Enter your nickname: ")
        time.sleep(1)
        print(f" | System: Nice name, {name}!")
        time.sleep(1)
        print(" | System: Now, please choose your tutor:")
        time.sleep(1)
        print(" " * 60, "-------------------------------------")
        time.sleep(0.25)
        print(" " * 60, "| 1. Regina                         |")
        time.sleep(0.25)
        print(" " * 60, "| 2. Rodrick                        |")
        time.sleep(0.25)
        print(" " * 60, "| 3. Julien                         |")
        time.sleep(0.25)
        print(" " * 60, "| 4. System                         |")
        time.sleep(0.25)
        print(" " * 60, "-------------------------------------")
        time.sleep(1)
        tutor = input(" | Who do you prefer? (1-4): ")
        while tutor not in ["1", "2", "3", "4"]:
            tutor = input(" | Please enter a valid input: ")
        time.sleep(1)
        if tutor == "1":
            print(" | System: Regina? Well, we won't judge")
        elif tutor == "2":
            print(" | System: Rodrick? Good choice!")
        elif tutor == "3":
            print(" | System: Woah, haven't heard that name in a while...")
        time.sleep(1)

        if tutor in ["1", "2", "3"]:
            return tutor, name
        else:
            while True:
                if refusalCount == 0:
                    refusalCount += 1
                    print(" | System: Hey! You can't choose me!")
                    time.sleep(1)
                    print(" | System: Why am I even an option?\n")
                    time.sleep(1)
                    print(" " * 60, "-------------------------------------")
                    time.sleep(0.25)
                    print(" " * 60, "| 1. Regina                         |")
                    time.sleep(0.25)
                    print(" " * 60, "| 2. Rodrick                        |")
                    time.sleep(0.25)
                    print(" " * 60, "| 3. Julien                         |")
                    time.sleep(0.25)
                    print(" " * 60, "-------------------------------------")
                    tutor = input(" | System: Please choose another tutor: ")
                    time.sleep(1)
                    if tutor in ["1", "2", "3"]:
                        return tutor, name
                    else:
                        continue
                elif refusalCount == 1:
                    time.sleep(1)
                    tutor = str(random.choice(["1", "2", "3"]))
                    print(" | System: You know what? I'll choose for you.")
                    time.sleep(1)
                    return tutor, name
                else:
                    time.sleep(1)
                    tutor = str(random.choice(["1", "2", "3"]))
                    print(" | System: Trying this again? Give me a break.")
                    return tutor, name

    def mainMenu():
        while True:
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
            print("                                                 || 1. Start Game                                               ||")
            time.sleep(0.25)
            print("                                                 || 2. Instructions                                             ||")
            time.sleep(0.25)
            print("                                                 || 3. Achievements                                             ||")
            time.sleep(0.25)
            print("                                                 || 4. Credits                                                  ||")
            time.sleep(0.25)
            print("                                                 || 5. Quit                                                     ||")
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
        print()
        time.sleep(1)
        print(" " * 60, "================ PLAY ================")
        tutor, name = tutorSelection()
        print(" | System: Let me call them for you. In the meantime, customize your quiz so you can start immediately!\n")
        time.sleep(0.5)
        print(" " * 60, "-------------------------------------")
        time.sleep(0.25)
        print(" " * 60, "| 1. Identification                 |")
        time.sleep(0.25)
        print(" " * 60, "| 2. Multiple Choice                |")
        time.sleep(0.25)
        print(" " * 60, "-------------------------------------")
        time.sleep(1)
        quizChoice = input(" | What quiz type do you want? (1 or 2): ").strip()
        while quizChoice not in ["1", "2"]:
            quizChoice = input("\n Please Enter a valid answer ").strip()

        time.sleep(1)
        print(" " * 60, "-------------------------------------")
        time.sleep(0.25)
        print(" " * 60, "| 1. First Quarter                  |")
        time.sleep(0.25)
        print(" " * 60, "| 2. Second Quarter                 |")
        time.sleep(0.25)
        print(" " * 60, "| 3. Third Quarter                  |")
        time.sleep(0.25)
        print(" " * 60, "| 4. Fourth Quarter                 |")
        time.sleep(0.25)
        print(" " * 60, "-------------------------------------")
        time.sleep(1)
        quarterChoice = int(input(" | What quarter would you like to study? (1-4): ").strip())
        while quarterChoice not in [1, 2, 3, 4]:
            quarterChoice = input("\n Please Enter a valid answer ").strip()

        time.sleep(1)
        print(" " * 60, "-------------------------------------")
        time.sleep(0.25)
        print(" " * 60, "| Difficulty Options:               |")
        time.sleep(0.25)
        print(" " * 60, "| 1. Easy                           |")
        time.sleep(0.25)
        print(" " * 60, "| 2. Hard                           |")
        time.sleep(0.25)
        print(" " * 60, "-------------------------------------")
        time.sleep(1)
        diffChoice = input(" | What difficulty would you like to answer? (1 or 2): ").strip()
        time.sleep(1)
        if diffChoice == "1" and quizChoice == "1":
            questions = easyID
        elif diffChoice == "1" and quizChoice == "2":
            questions = easyMP
        elif diffChoice == "2" and quizChoice == "1":
            questions = hardID
        else:
            questions = hardMP

# ===================================================================================================================
# Run Quiz
        cont = "Y"
        gameEnd = "======================================================================== GAME END ========================================================================"
        tutorNames = {
            "1": "Regina",
            "2": "Rodrick",
            "3": "Julien"
        }

        for line in dialogue[tutorNames[tutor]]["intro"]:
            print(line)

        time.sleep(2.5)

        if cont == "Y":  # Checks if player chose to continue
            askedIndices = 0
            score = 0

            print(" " * 67, "----------------")  # Border
            print(" " * 67, "|Starting Round|")
            print(" " * 67, "----------------")  # Border

            while askedIndices < 5:  # Will check if the maximum amount of questions have already been asked
                filtered_questions = []

                for q in questions:
                    if q["quarter"] == quarterChoice:
                        filtered_questions.append(q)

                q = filtered_questions[askedIndices]

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

                if quizChoice == "2":
                    print(q["options"])

                # Input Validation
                print("=" * 36)
                if quizChoice == "2":
                    userAnswer = input(">>> Please enter your answer (A/B/C/D): ").upper().strip()
                    while userAnswer not in ["A", "B", "C", "D"]:
                        userAnswer = input(">>> Invalid answer. Please enter A, B, C, or D: ").upper().strip()
                else:
                    userAnswer = input(">>> Enter your answer: ").strip().capitalize()

                # Checks if users answer is correct or not
                if userAnswer == q["answer"]:
                    print(dialogue[tutorNames[tutor]]["correct"])
                    score += 1
                else:
                    print(dialogue[tutorNames[tutor]]["incorrect"])
                time.sleep(1)
                print("\n>>> Answer: ", q["answer"])
                time.sleep(2)
                askedIndices += 1 # Adds one to the variable to show one question has already been answered

                # Asks player if they want to continue
                if askedIndices < 5:  # Checks if the amount of asked questions is lesser than questions per era
                    print("=" * 33)
                    cont = input(dialogue[tutorNames[tutor]]["continue"]).upper().strip()
                    while cont not in ["Y", "N"]:  # Input Validation
                        cont = input("Invalid input. Do you want to continue? (Y/N): ").upper().strip()
                    if cont == "N":  # If player chose to not continue
                        print(dialogue[tutorNames[tutor]]["no"])
                        time.sleep(1.5)
                        print(gameEnd, "\n")
                        break  # Terminates loop
                    else:
                        print(dialogue[tutorNames[tutor]]["yes"])
                        continue  # Stops the while loop but continues the for loop

                # Outcome of round
                if askedIndices == 5:
                    print("\n" + "-" * 150)  # Border
                    time.sleep(1.5)
                    print(f" | System: Your score is {score} out of 5-")  # Displays score
                    time.sleep(0.25)
                    print(dialogue[tutorNames[tutor]]["final"][score])
                    time.sleep(1.5)
                    print("\n | System: Well you two have certainly gotten close.")
                    time.sleep(0.5)
                    print(" | System: ...")
                    time.sleep(2)
                    print(" | System: That's enough for now.")
                    time.sleep(1)
                    print(" | System: See you soon!")
                    input("Press Enter to go to menu")  # Provides a brief period of time for players to read/reflect
                    time.sleep(1)
                    time.sleep(0.5)
                    return
        else:
            return

    def instructionsOption():
        print("\n", " " * 60, " ============= INSTRUCTIONS ============")
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
        print("\n", " " * 60, " ============= ACHIEVEMENTS ============")
        print(" | Uh oh! That isn't available yet! This will be added soon :D")

        input(" | Press ENTER to continue")

        print("\n" + "-" * 221, "\n")


    def creditsOption():
        print("\n", " " * 60, " =============== CREDITS ===============")
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

    print("=" * 72, "BIOQUEST", "=" * 72)
    # Welcome Statement
    time.sleep(3)
    print(" | Hi! and welcome to...")
    time.sleep(3)
    print("                                                           _____  _       _____                 _   ")
    print("                                                          | ___ )(_)_____| _   |_   _  ___  ___| |_ ")
    print("                                                          |  _  || |  _  | | | | | | |/ _ |/ __| __|")
    print("                                                          | |_) || | (_) | |_| | |_| |  __||__ | |_ ")
    print("                                                          |_____)|_|_____|___(_|_____|____||___|___|")
    time.sleep(2)
    print("\n | This is a quizzer, wherein you try your best to answer a series of questions correctly.")
    time.sleep(2)
    print(" | Make sure to have fun!")
    time.sleep(2)
    print(" | Try to explore more before trying out the main game")
    time.sleep(2)
    print(" | Anyways, enjoy!")
    mainMenu()

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

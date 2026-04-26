# Standard libraries used for timing, randomness, file handling, and data storage
import time
import random
import json
import csv
import os
from datetime import datetime

# ===================================================================================================================
# Saves quiz results into a CSV file for achievement tracking
def saveScore(name, quizChoice, score, tutor):
    today = str(datetime.now().date())

    # Maps stored IDs to readable names
    tutorNames = {
        "1": "Regina",
        "2": "Rodrick",
        "3": "Julien"
    }
    quizNames = {
        "1": "Identification",
        "2": "Multiple Choice"
    }

    # Check if file exists to determine whether headers should be written
    file_exists = os.path.isfile("achievements.csv")

    with open("achievements.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "name", "quiz", "score", "tutor"])

        # Write header only for a new file
        if not file_exists:
            writer.writeheader()

        # Save one quiz attempt
        writer.writerow({
            "date": today,
            "name": name,
            "quiz": quizNames[quizChoice],
            "score": score,
            "tutor": tutorNames[tutor]
        })

# ===================================================================================================================
try:
    # Load quiz data from JSON files (different difficulty levels and formats)
    with open("easyQuestionsMP.json", 'r', encoding="utf-8") as file:
        easyMP = json.load(file)

    with open("hardQuestionsMP.json", 'r', encoding="utf-8") as file:
        hardMP = json.load(file)

    with open("easyID.json", 'r', encoding="utf-8") as file:
        easyID = json.load(file)

    with open("hardID.json", 'r', encoding="utf-8") as file:
        hardID = json.load(file)

    with open("dialogue.json", 'r', encoding="utf-8") as file:
        dialogue = json.load(file)

# ===================================================================================================================
# Handles tutor selection and player identity setup
    def tutorSelection():
        refusalCount = 0

        # Initial system greeting
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

        # Tutor selection menu
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
        
        while tutor not in ["1", "2", "3", "4"]: # Input Validation
            tutor = input(" | Please enter a valid input: ")
        time.sleep(1)

        # Simple feedback based on selection
        if tutor == "1":
            print(" | System: Regina? Well, we won't judge")
        elif tutor == "2":
            print(" | System: Rodrick? Good choice!")
        elif tutor == "3":
            print(" | System: Woah, haven't heard that name in a while...")
        time.sleep(1)

        # Normal valid tutors
        if tutor in ["1", "2", "3"]:
            return tutor, name

        # Special case: user tries selecting "System"
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

                # Auto-assign tutor after repeated invalid attempts
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

# ===================================================================================================================
# Displays and handles main menu navigation
    def mainMenu():
        while True:
            # Main Menu ASCII Art
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

            # Validate menu input
            while menuChoice not in ["1", "2", "3", "4", "5"]:
                menuChoice = input("\n Please Enter a valid answer: ").strip()

            # Clear screen (visual spacing)
            for x in range(100):
                print()

            # Route user choice to correct function
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

# ===================================================================================================================
# Main gameplay function (quiz system)
    def playOption():
        print()
        time.sleep(1)
        print(" " * 60, "================ PLAY ================")
        
        tutor, name = tutorSelection()
        
        print(" | System: Let me call them for you. In the meantime, customize your quiz so you can start immediately!\n")

        # Quiz type selection
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

        # Quarter selection
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
            quarterChoice = int(input("\n Please Enter a valid answer ").strip())

        # Difficulty selection
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
        
        while diffChoice not in ["1", "2", "3", "4"]: 
            diffChoice = input("\n Please Enter a valid answer ").strip()
        time.sleep(1)

        # Assign question set
        if diffChoice == "1" and quizChoice == "1":
            questions = easyID
        elif diffChoice == "1" and quizChoice == "2":
            questions = easyMP
        elif diffChoice == "2" and quizChoice == "1":
            questions = hardID
        else:
            questions = hardMP

# ===================================================================================================================
# QUIZ ENGINE (handles question flow, scoring, and early exit system)
        
        # Game control variables
        cont = "Y"
        gameEnd = "======================================================================== GAME END ========================================================================"
        tutorNames = {
            "1": "Regina",
            "2": "Rodrick",
            "3": "Julien"
        }

        # Display tutor-specific intro dialogue before quiz starts
        for line in dialogue[tutorNames[tutor]]["intro"]:
            print(line)

        time.sleep(2.5)

        # Only runs quiz if user chose to continue
        if cont == "Y": 
            
            # Tracks Progress
            askedIndices = 0
            score = 0

            # Filter questions based on selected quarter (curriculum-based grouping)
            filtered_questions = [
                q for q in questions
                if q["quarter"] == quarterChoice
            ]

            # Safety check: prevents crash if no matching questions exist
            if not filtered_questions:
                print("No questions found for this quarter.")
                return

            # Main quiz loop (max 5 questions)
            while askedIndices < 5: 
                
                q = filtered_questions[askedIndices]

                # Display progress indicator
                time.sleep(1.5)
                print("\n" + " " * 60, "=" * 30)
                print(" " * 60, f"=           {askedIndices + 1} of 5           =")
                print(" " * 60, "=" * 30)

                # Show question prompt
                time.sleep(1.5)
                print("-" * 100)
                print(q["question"])
                print("-" * 100)
                time.sleep(1.5)

                # Show multiple choice options only if needed
                if quizChoice == "2":
                    print(q["options"])

                print("=" * 36) # Border

                # Collect user answer with validation based on quiz type
                if quizChoice == "2":
                    userAnswer = input(">>> Please enter your answer (A/B/C/D): ").upper().strip()
                    while userAnswer not in ["A", "B", "C", "D"]:
                        userAnswer = input(">>> Invalid answer. Please enter A, B, C, or D: ").upper().strip()
                else:
                    userAnswer = input(">>> Enter your answer: ").strip().capitalize()

                # Check correctness of answer
                if userAnswer == q["answer"]:
                    print(dialogue[tutorNames[tutor]]["correct"])
                    score += 1
                else:
                    print(dialogue[tutorNames[tutor]]["incorrect"])
                time.sleep(1)
                print("\n>>> Answer: ", q["answer"])
                time.sleep(2)
                
                askedIndices += 1 # Move to next question

                # Early exit option (user-controlled pacing)
                if askedIndices < 5:
                    print("=" * 33)
                    cont = input(dialogue[tutorNames[tutor]]["continue"]).upper().strip()

                    # Validate continue input
                    while cont not in ["Y", "N"]:  # Input Validation
                        cont = input("Invalid input. Do you want to continue? (Y/N): ").upper().strip()
                        
                    if cont == "N":  # If player chose to not continue
                        print(dialogue[tutorNames[tutor]]["no"])
                        time.sleep(1.5)
                        print(gameEnd, "\n")
                        break
                    else: # If player chooses to continue
                        print(dialogue[tutorNames[tutor]]["yes"])
                        continue 

                # Final result display after quiz ends
                if askedIndices == 5: # Checks if asked questions is equivalent to the maximum questions
                    print("\n" + "-" * 150)  # Border
                    time.sleep(1.5)
                    
                    print(f" | System: Your score is {score} out of 5-")  # Displays score
                    time.sleep(0.25)

                    # Ending dialogue depends on performance
                    print(dialogue[tutorNames[tutor]]["final"][score])
                    
                    time.sleep(1.5)
                    print("\n | System: Well you two have certainly gotten close.")
                    time.sleep(1)
                    print(" | System: ...")
                    time.sleep(2)
                    print(" | System: That's enough for now.")
                    time.sleep(1)
                    print(" | System: See you soon!")
                    input("Press Enter to go to menu")  

                    # Save results for achievement tracking
                    saveScore(name, quizChoice, score, tutor)
                    
                    time.sleep(0.5)

                    # Screen clear effect
                    for x in range(50):
                        print()
                    return
        else:
            return

# ===================================================================================================================
# Instructions screen (explains how the system works)
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

# ===================================================================================================================
# Achievement viewer (reads stored quiz results from CSV)
    def achievementsOption():
        print("\n", " " * 60, " ============= ACHIEVEMENTS ============")
        scores = []
        hasData = False  # Track if the code actually reads anything

        try:
            with open("achievements.csv", "r") as f:
                reader = csv.DictReader(f)

                # Read and display each stored attempt
                for i, row in enumerate(reader, start=1):

                    # Skip invalid rows
                    if not row["score"]: 
                        continue

                    hasData = True

                    score = int(row["score"])
                    scores.append(score)

                    print("\n=== Achievement Log ===")
                    print(f">>> [{i}] {row['date']} | {row['name']} | {row['quiz']} | {score}/5 | {row['tutor']}")

            # If no data exists yet
            if not hasData:
                print(" | No achievements yet. Play a quiz first!")

            # Performance summary
            elif scores:
                avg = sum(scores) / len(scores) * 100
                print(f"\nAverage Score: {avg:.2f}%")
                print(f"Total Attempts: {len(scores)}")

        except FileNotFoundError:
            print("No records found yet.")

        input(" | Press ENTER to continue")

        print("\n" + "-" * 221, "\n")

# ===================================================================================================================
# Credits screen (project contributors)
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

# ===================================================================================================================
# PROGRAM START (welcome screen + entry point)
    
    print("=" * 72, "BIOQUEST", "=" * 72)
    
    time.sleep(3)
    print(" | Hi! and welcome to...")
    time.sleep(3)
    # ASCII Title Banner
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

# ===================================================================================================================
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")

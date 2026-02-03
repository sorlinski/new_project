import os

def grade_tracker():
    filename = "my_grades.txt"

    print("Welcome to your Grade Tracker")
    print("Type 'G' to Add a Grade, 'V' to View Average, or 'Q' to Quit.")

    while True:
        choice = input("\nWhat would you like to do? (G/V/Q): ").upper()

        if choice == 'G':
            try:
                subject = input("Enter Subject: ")
                grade = float(input(f"Enter grade for {subject}: "))
                
                with open(filename, "a") as file:
                    file.write(f"{subject}:{grade}\n")
                print("Success! Grade saved.")

            except ValueError:
                print("Error. Please enter a number for the grade (like 90 or 85.5).")

        elif choice == 'V':
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                    
                    # Extract just the numbers from each line
                    scores = [float(line.split(":")[1]) for line in lines]
                    
                    if scores:
                        avg = sum(scores) / len(scores)
                        print(f"You have {len(scores)} subjects recorded.")
                        print(f"Your current average is: {avg:.2f}")
                    else:
                        print("No Data")

            except FileNotFoundError:
                print("No records found. Add a grade first!")

        elif choice == 'Q':
            print("Goodbye! Good luck with your studies.")
            break
        else:
            print("Invalid choice. Just type G, V, or Q.")

# Start the program
grade_tracker()

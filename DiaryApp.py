import datetime

def diary_app():
    filename = "my_diary.txt"
    choice = input("Do you want to (W)rite or (V)iew? ").upper()

    try:
        if choice == 'W':
            # 'a' opens for appending (adding to the end)
            with open(filename, "a") as file:
                note = input("Enter your thought: ")
                time = datetime.datetime.now().strftime("%H:%M")
                file.write(f"{time}: {note}\n")
                print("Saved!")

        elif choice == 'V':
            # 'r' opens for reading
            with open(filename, "r") as file:
                print("\n--- Past Entries ---\n" + file.read())

    except FileNotFoundError:
        print("No diary found yet. Write something first!")
    except PermissionError:
        print("System error: Permission denied.")

diary_app()

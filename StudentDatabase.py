class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        avg = self.calculate_average()
        print(f"Name: {self.name:<15} | Age: {self.age:<3} | Avg: {avg:.2f}")

def main():
    students = []
    
    while True:
        print("\n--- Student Management System ---")
        print("[1] Add Student  [2] View All  [3] Delete Student  [4] Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            raw_grades = input("Enter grades (comma-separated): ")
            try:
                grades_list = [int(g.strip()) for g in raw_grades.split(",")]
                students.append(Student(name, age, grades_list))
                print(f"Added {name}.")
            except ValueError:
                print("Invalid grades format.")

        elif choice == '2':
            print("\n--- Current Database ---")
            if not students: print("Database empty.")
            for s in students: s.display_info()

        elif choice == '3':
            name_to_delete = input("Enter the name of the student to remove: ")
            initial_count = len(students)
            
            students = [s for s in students if s.name.lower() != name_to_delete.lower()]
            
            if len(students) < initial_count:
                print(f"Successfully deleted {name_to_delete}.")
            else:
                print(f"Student '{name_to_delete}' not found.")

        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
    
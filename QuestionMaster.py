import csv
import os

'''Created by
        SivaVenna
            21/09/2024'''
# File path for the question CSV
QUESTION_FILE = 'questions.csv'


def read_questions():
    """Read questions from the CSV file."""
    questions = []
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
    return questions


def write_questions(questions):
    """Write questions to the CSV file."""
    with open(QUESTION_FILE, 'w', newline='') as file:
        fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for question in questions:
            writer.writerow(question)


def display_menu():
    """Display the menu options."""
    print("1) Add a question")
    print("2) Search for a Question based on question num")
    print("3) Delete question based on question num")
    print("4) Modify the question based on question num")
    print("5) Display all the questions")
    print("6) Exit menu")


def add_question(questions):
    """Add a new question to the list."""
    num = len(questions) + 1
    question = input("Enter the question: ")
    option1 = input("Enter option 1: ")
    option2 = input("Enter option 2: ")
    option3 = input("Enter option 3: ")
    option4 = input("Enter option 4: ")
    correctoption = input("Enter the correct option ( 1 - 4 ): ")

    questions.append({
        'num': str(num),
        'question': question,
        'option1': option1,
        'option2': option2,
        'option3': option3,
        'option4': option4,
        'correctoption': correctoption
    })
    write_questions(questions)
    print("Question added successfully!")


def search_question(questions):
    """Search for a question by its number."""
    num = input("Enter the question number to search: ")
    for question in questions:
        if question['num'] == num:
            print(question)
            return
    print("Question not found.")


def delete_question(questions):
    """Delete a question by its number."""
    num = input("Enter the question number to delete: ")
    for question in questions:
        if question['num'] == num:
            questions.remove(question)
            write_questions(questions)
            print("Question deleted successfully!")
            return
    print("Question not found.")


def modify_question(questions):
    """Modify an existing question."""
    num = input("Enter the question number to modify: ")
    for question in questions:
        if question['num'] == num:
            question['question'] = input("Enter the new question: ")
            question['option1'] = input("Enter new option 1: ")
            question['option2'] = input("Enter new option 2: ")
            question['option3'] = input("Enter new option 3: ")
            question['option4'] = input("Enter new option 4: ")
            question['correctoption'] = input("Enter the correct option (e.g., option1, option2, etc.): ")
            write_questions(questions)
            print("Question modified successfully!")
            return
    print("Question not found.")


def display_all_questions(questions):
    """Display all questions."""
    for question in questions:
        print(question)


def main():
    """Main function to run the question master."""
    questions = read_questions()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_question(questions)
        elif choice == '2':
            search_question(questions)
        elif choice == '3':
            delete_question(questions)
        elif choice == '4':
            modify_question(questions)
        elif choice == '5':
            display_all_questions(questions)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

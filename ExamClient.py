import csv
import os
import logging
import datetime


'''Contributed by Srujan & VaraPrasad 21/sept/2024'''
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# File paths for the question CSV and log file
QUESTION_FILE = 'questions.csv'
LOG_FILE = 'exam_attempts.log'


def read_questions():
    """Read questions from the CSV file."""
    questions = []
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                questions.append(row)
    return questions


def log_attempt(student_name, university, score, total_questions):
    """Log the exam attempt to a log file."""
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(
            f"{datetime.datetime.now()} - {student_name} from {university} scored {score} out of {total_questions}\n"
        )


def take_exam(questions):
    """Conduct the exam by asking questions and recording the score."""
    student_name = input("Enter student name: ")
    university = input("Enter university: ")
    score = 0

    for question in questions:
        print(f"Q{question['num']}: {question['question']}")
        print(f"  1) {question['option1']}")
        print(f"  2) {question['option2']}")
        print(f"  3) {question['option3']}")
        print(f"  4) {question['option4']}")
        answer = input("Enter your choice (1/2/3/4): ")
        if answer == question['correctoption']:
            score += 1

    print(f"\nStudent name = {student_name}")
    print(f"University = {university}")
    print(f"Marks-scored = {score} correct out of {len(questions)} questions")

    # Log the attempt
    log_attempt(student_name, university, score, len(questions))


def main():
    """Main function to run the exam client."""
    print(f"Today's date and time: {datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S')}")
    questions = read_questions()
    if not questions:
        print("No questions available. Please add questions using the QuestionMaster.")
        return
    take_exam(questions)


if __name__ == "__main__":
    main()

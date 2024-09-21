import pandas as pd
import logging
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ExamClient:
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()

    def load_questions(self):
        try:
            df = pd.read_csv(self.filename)
            questions = df.to_dict(orient='records')
            logging.info("Questions loaded successfully.")
            return questions
        except Exception as e:
            logging.error(f"Error loading questions: {e}")
            return []

    def take_exam(self):
        student_name = input("Enter student name: ")
        university = input("Enter university: ")
        score = 0

        for question in self.questions:
            print(f"Q{question['num']}: {question['question']}")
            print(f"  1) {question['option1']}")
            print(f"  2) {question['option2']}")
            print(f"  3) {question['option3']}")
            print(f"  4) {question['option4']}")
            answer = input("Enter your choice (option1/option2/option3/option4): ")
            if answer == question['correct option']:
                score += 1

        print(f"\nStudent name = {student_name}")
        print(f"University = {university}")
        print(f"Marks-scored = {score} correct out of {len(self.questions)} questions")

def main():
    print(f"Today's date and time: {datetime.datetime.now().strftime('%d/%b/%Y %H:%M:%S')}")
    ec = ExamClient('questions.csv')
    ec.take_exam()

if __name__ == "__main__":
    main()

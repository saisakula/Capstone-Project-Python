import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuestionMaster:
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

    def save_questions(self):
        try:
            df = pd.DataFrame(self.questions)
            df.to_csv(self.filename, index=False)
            logging.info("Questions saved successfully.")
        except Exception as e:
            logging.error(f"Error saving questions: {e}")

    def add_question(self, question, option1, option2, option3, option4, correct_option):
        num = len(self.questions) + 1
        new_question = {
            'num': str(num),
            'question': question,
            'option1': option1,
            'option2': option2,
            'option3': option3,
            'option4': option4,
            'correct option': correct_option
        }
        self.questions.append(new_question)
        self.save_questions()

    def search_question(self, num):
        for question in self.questions:
            if question['num'] == str(num):
                return question
        return None

    def delete_question(self, num):
        self.questions = [q for q in self.questions if q['num'] != str(num)]
        self.save_questions()

    def modify_question(self, num, question, option1, option2, option3, option4, correct_option):
        for q in self.questions:
            if q['num'] == str(num):
                q['question'] = question
                q['option1'] = option1
                q['option2'] = option2
                q['option3'] = option3
                q['option4'] = option4
                q['correct option'] = correct_option
                self.save_questions()
                return
        logging.warning(f"Question number {num} not found.")

    def display_questions(self):
        for question in self.questions:
            print(f"Q{question['num']}: {question['question']}")
            print(f"  1) {question['option1']}")
            print(f"  2) {question['option2']}")
            print(f"  3) {question['option3']}")
            print(f"  4) {question['option4']}")
            print(f"  Correct Option: {question['correct option']}")
            print()

def main():
    qm = QuestionMaster('questions.csv')
    while True:
        print("1) Add a question")
        print("2) Search for a Question based on question num")
        print("3) Delete question based on question num")
        print("4) Modify the question based on question num")
        print("5) Display all the questions")
        print("6) Exit menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            question = input("Enter the question: ")
            option1 = input("Enter option 1: ")
            option2 = input("Enter option 2: ")
            option3 = input("Enter option 3: ")
            option4 = input("Enter option 4: ")
            correct_option = input("Enter the correct option (option1/option2/option3/option4): ")
            qm.add_question(question, option1, option2, option3, option4, correct_option)
        elif choice == '2':
            num = input("Enter question number to search: ")
            question = qm.search_question(num)
            if question:
                print(question)
            else:
                print("Question not found.")
        elif choice == '3':
            num = input("Enter question number to delete: ")
            qm.delete_question(num)
        elif choice == '4':
            num = input("Enter question number to modify: ")
            question = input("Enter the question: ")
            option1 = input("Enter option 1: ")
            option2 = input("Enter option 2: ")
            option3 = input("Enter option 3: ")
            option4 = input("Enter option 4: ")
            correct_option = input("Enter the correct option (option1/option2/option3/option4): ")
            qm.modify_question(num, question, option1, option2, option3, option4, correct_option)
        elif choice == '5':
            qm.display_questions()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

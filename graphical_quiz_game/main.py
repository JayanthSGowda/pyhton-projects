from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for entry in question_data:
    question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


# print("You've completed the quiz")
# print(f"Your final score is: {quiz.score}/{quiz.question_number}")

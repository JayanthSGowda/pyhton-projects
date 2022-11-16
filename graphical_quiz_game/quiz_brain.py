import html
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self) -> bool:
        return not self.question_number == len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q{self.question_number}: {html.unescape(question.text)}"
        # answer = input(f"Q{self.question_number}: {html.unescape(question.text)} (True/False): ")
        # self.check_answer(answer, question.answer)

    def check_answer(self, u_answer):
        if u_answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            self.score += 1
            return True
        else:
            return False
        # print(f"The correct answer is {c_answer}.")
        # print(f"Your current score is: {self.score}/{self.question_number}.\n")




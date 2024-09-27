

class QuziBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
    # here question_list  is use for inside of class body but q_list use outside of class body
        self.score = 0


    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num} : {current_question.text} ? (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You got it right! ")
        else:
            print("You got it wrong")
        print(f"Answer was {current_answer}, Your current score: {self.score}/{self.question_num}\n")
from question_model import Question
from data import question_data
from quiz_brain import QuziBrain

question_bank = [

]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

current_q = QuziBrain(question_bank)

while current_q.still_has_question():
    current_q.next_question()

print("You've completed the quiz")
print(f"Your final score was {current_q.score}/{len(question_bank)}")

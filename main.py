from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    ques = item["question"]
    answ = item["correct_answer"]

    new_question = Question(ques, answ)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"your final score was: {quiz.score} / {quiz.question_number}")
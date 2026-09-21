class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list


    # Next question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q {self.question_number}. {current_question.question}: ")
        self.check_answer(user_answer, current_question)
    

    # still has question
    def still_has_question(self):
        return self.question_number < len(self.question_list)
    

    # Check Correct answer
    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("Yes, you got it.")
        else:
            print("You're wrong!")

        print(f"Correct answer is: {current_question.answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")



class Survey:

    def __init__(self, qualifying_questions):
        self.qualifying_questions = qualifying_questions
        self.user_answers_qualifying = []

    def start_survey(self):
        print()
        print('She Codes Plus Survey')
        print()
        print('You will be asked a series of multiple choice questions which will help provide feedback on the She Codes Plus course')
        print()
        print('To record your answer, simply type a, b, c or d, and press the Enter key')
        print()

    def ask_qualifying_questions(self):
        for question in self.qualifying_questions:
            print(question.question_text)
            print(question.answers)
            print()
            user_response = input()
            self.user_answers_qualifying.append(user_response)
            print()

    def end():
        pass
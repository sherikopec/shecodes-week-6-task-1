class Section:

    def __init__(self):
        self.qualifying_question = qualifying_question
        self.first_question = first_question
        self.description = description

    def start_saturday_section(self):
        print()
        print(self.description)
        print()
        for question in self.questions:
            print(question.question_text)
            print(question.answers)
            print()
            input()
            print()
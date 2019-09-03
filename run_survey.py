from Survey import Survey
from Question import Question
from Answer import Answer
from Section import Section

# Set up qualifying questions into a list with Question class
qualifying_questions = [
    Question('Do you attend Wednesday night tutorials?', '(a) Yes\n(b) No'),
    Question('Do you attend Saturday workshops?', '(a) Yes\n(b) No')
]

wednesday_questions = [
    Question('Question 1', '(a) \n(b) \n(c) \n(d) \n'),
    Question('Question 2', '(a) \n(b) \n(c) \n(d) \n'),
    Question('Question 3', '(a) \n(b) \n(c) \n(d) \n')
]

saturday_questions = [
    Question('Question 1', '(a) \n(b) \n(c) \n(d) \n'),
    Question('Question 2', '(a) \n(b) \n(c) \n(d) \n'),
    Question('Question 3', '(a) \n(b) \n(c) \n(d) \n')
]

# Create a new instance of the Survey class called my_survey and pass it the qualifying questions
my_survey = Survey(qualifying_questions)

# Run the start survey method on the new instance of Survey
my_survey.start_survey()

# Run the ask qualifying questions method
my_survey.ask_qualifying_questions()

# Create a new instance of the Section class called wednesday_section
wednesday_section = Section('This section will ask you 3 questions about the Wednesday night tutorials', wednesday_questions)
saturday_section = Section('This section will ask you 3 questions about the Saturday workshops', saturday_questions)

# Run the wednesday section IF qualifying question 1 was answered with 'a'
if my_survey.user_answers_qualifying[0] == 'a':
    wednesday_section.start_wednesday_section()
else:
    print('Catch up section')

if my_survey.user_answers_qualifying[1] == 'a':
    saturday_section.start_saturday_section()
else:
    print('Catch up section')
    print()

# End the survey
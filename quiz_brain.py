import re

class QuizBrain:

    def __init__( self, q_list ):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.no_of_questions_to_ask = 10
        self.page_width = 70

    def nice_text( self, question ):
        if len(question) < self.page_width:
            return question

        spaces = []
        found_spaces = [c.start() for c in re.finditer(' ', question)]
        for position in found_spaces:
            if position < self.page_width:
                spaces.append(position)
        lastspace =  spaces.pop()
        new_string = question[:lastspace] + '\n   ' + question[lastspace:]
        return new_string


    def question( self, q_number ):
        self.question_number += 1
        message = \
            f"Question {self.question_number}: \n" \
            f"    {self.nice_text(q_number.text)}\n       " \
            f"(True/False)?: "


        response = input(message).lower()[:1]
        if response == 't':
            response = 'True'
        else:
            response = 'False'

        return q_number.answer == response

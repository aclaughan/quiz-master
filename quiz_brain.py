class QuizBrain:

    def __init__( self, q_list ):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def question( self ):
        message = \
            f"Q.{self.question_number +1}: " \
            f"{self.question_list[self.question_number].text} " \
            f"(True/False)?: "

        self.question_number += 1
        response = input(message).lower()[:1]
        if response == 't':
            response = 'True'
        else:
            response = 'False'

        return self.question_list[self.question_number -1].answer == response

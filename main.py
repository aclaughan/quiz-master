from data import question_data
import logging
from question_model import Question
from quiz_brain import QuizBrain
from art import logo
import random
from pprint import pprint, pformat

logging.basicConfig(level = logging.DEBUG)


def main():
    print(logo)
    question_bank = []
    num_of_questions = len(question_data)

    for i in range(num_of_questions):
        question_bank.append(
            Question(question_data[i]["text"], question_data[i]["answer"]))

    Quizzer = QuizBrain(question_bank)
    questions = random.sample(question_bank, Quizzer.no_of_questions_to_ask)

    print(f"I found {num_of_questions} questions.")
    print(
        f"I have chosen {Quizzer.no_of_questions_to_ask} random questions\n" \
        f"to ask you. Good luck :)\n" )

    while questions:
        if Quizzer.question(questions.pop()):
            Quizzer.score += 1
            print(f'Correct, you earn a point [{Quizzer.score}/{Quizzer.no_of_questions_to_ask}]\n')

        else:
            print('That is incorrect\n')

    print(f"final score: {Quizzer.score}/{Quizzer.no_of_questions_to_ask}")


if __name__ == '__main__':
    main()

# logging.debug(stuff)

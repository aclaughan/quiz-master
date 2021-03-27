from data import question_data
import logging
from question_model import Question
from quiz_brain import QuizBrain
from art import logo
from pprint import pprint, pformat

logging.basicConfig(level = logging.DEBUG)


def main():
    print(logo)
    question_bank = []
    for i in range(len(question_data)):
        question_bank.append(
            Question(question_data[i]["text"], question_data[i]["answer"]))

    # message = pformat(question_bank, indent=2, sort_dicts = False)
    # logging.info(message)

    Quizzer = QuizBrain(question_bank)
    for i in range(len(question_bank)):
        if Quizzer.question():
            print('Correct, you earn a point')
            Quizzer.score += 1
        else:
            print('That is incorrect')

    print(f"final score: {Quizzer.score}")


if __name__ == '__main__':
    main()

# logging.debug(stuff)

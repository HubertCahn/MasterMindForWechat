import random
import time
"""Master mind, a mini game for guessing number
"""


def random_num_generator(length, repeatable=False):
    """
    Generate a number in specific length. If repeatable is true, the number in
    different position can be the same one.

    :type length: int
    :param length: the length of the number

    :type repeatable: boolean
    :param repeatable: whether the number in different position can be same

    :rtype: str
    :return: a random number
    """
    if repeatable:
        number_list = [random.randint(0, 9) for _ in range(length)]
    else:
        number_list = random.sample(range(10), length)
    random_num = ''.join(map(str, number_list))
    return random_num


def number_judger(true_answer, user_answer):
    """
    Distinguish the difference between the true answer and user answer

    :type true_answer: str
    :param true_answer: the true answer of this game

    :type user_answer: str
    :param user_answer: the answer from user

    :rtype: tuple
    :return: a tag to indicate whether the user's answer is correct or not, and
                        the hints of their difference
    """
    tag = True
    # number is correct, but position is wrong
    hint_cnwp = 0
    # both number and position are correct
    hint_cncp = 4

    if user_answer != true_answer:
        tag = False

        for pos, value in enumerate(user_answer):
            if value != true_answer[pos]:
                hint_cncp -= 1
            else:
                true_answer = true_answer[:pos] + 'r' + true_answer[pos + 1:]

        for value in user_answer:
            hint_cnwp = hint_cnwp + 1 if value in true_answer else hint_cnwp

    return tag, hint_cnwp, hint_cncp


if __name__ == '__main__':

    is_finished = False
    count = 0
    start = time.time()
    TRUE_ANSWER = random_num_generator(4)

    print('Game started!')

    while not is_finished:
        count += 1
        user_input = input('Please input your answer:')
        judge_result = number_judger(TRUE_ANSWER, user_input)
        is_finished = judge_result[0]
        if not is_finished:
            message = 'Sorry, your answer is not correct. (Hints: correct number ' \
                            'but wrong position: {0}; correct number and correct position:' \
                            ' {1}'.format(judge_result[1], judge_result[2])
            print(message)

    end = time.time()
    message = 'Congratulations! You got the right answer in {0} seconds and {1} steps.'.format(
        int(end - start), count
    )
    print(message)

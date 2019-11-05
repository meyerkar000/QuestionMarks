# Kara Meyer
# 10-21-2019
# This program will return the value "true" if there are three question
# marks between and couple of numbers that add to 10.

# REQUIREMENTS:
"""
Returns true if exactly three question marks are between every instance
of two sequential numbers, whose sum is 10, in a string.
"""


def three_marks(UserInput):
    # Define a string with numbers, letters, and question marks
    # UserInput = "abc1???9???6???9"

    # Define your variables
    ThreeMarks = False
    NumberSum = 0
    QuestionCount = 0
    NumberList = []
    IndexList = []

    # Fill the NumberList and IndexList arrays with the info from the UserInput
    for index, character in enumerate(UserInput):
        if character.isdigit():
            NumberList.append(int(character))
            IndexList.append(index)

    # Test if the numbers add to 10 and if there are three ? between them
    for x in range(len(NumberList)-1):
        NumberSum = NumberList[x] + NumberList[x + 1]
        if NumberSum == 10:
            for character in UserInput[IndexList[x]:IndexList[x + 1]]:
                if character == "?":
                    QuestionCount += 1
            if QuestionCount == 3:
                ThreeMarks = True
                QuestionCount = 0  # reset QuestionCount
            else:
                ThreeMarks = False
                break

    # Print the answer
    # if all requirements are met then this should print true. Otherwise this
    # should print false
    return ThreeMarks


''' ========[ Test Cases ]========
'''
test_cases = [{'name': 'test_a',
               'val': "aa6?9",
               'answer': False},
              {'name': 'test_b',
               'val': "acc?7??sss?3rr1??????5",
               'answer': True},
              {'name': 'test_c',
               'val': "a?cc?7??sss33rr1??5???5",
               'answer': False},
              {'name': 'test_b',
               'val': "acc?7??sss?3rr1???5?zz??5",
               'answer': True}]


def test_question_marks():
    for test in test_cases:
        result = three_marks(test['val'])
        if result != test['answer']:
            result_str = ("Expected: {}".format(test['answer']))
        else:
            result_str = ("Correct!")

        print("{}".format(test['name']))
        print("{} : {}".format(result, test['val']))
        print(result_str)
        print("--------------------")


test_question_marks()

#!/usr/bin/env python
"""Game even or no even"""

from brain_games.engine import generation_question, answer, welcome


def main():
    name = welcome()
    count = 0
    while True:
        question = generation_question()
        ent = answer()
        if question == ent:
            print('Correct!')
            count += 1
        else:
            print(f"'{ent}' is wrong answer ;(. Correct answer was '{question}"
                  f"'.\nLet's try again, {name}")
            break
        if count == 3:
            print(f'Congratulations, {name}!')
            break


if __name__ == '__main__':
    main()

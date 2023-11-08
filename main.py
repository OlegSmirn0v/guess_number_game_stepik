from random import randint

print('Welcome to "The guess the number game!"')


def is_valid(num):
    while True:
        if num == 'q':
            exit_game()
        elif num.isdigit() is False or int(num) <= 0:
            print(
                f'Not number or lower than zero. Try again or press "q" to quit game.')
            num = input()
        else:
            return int(num)


def check_guess(guess, riddle_num):
    if guess < riddle_num:
        return 'Your number is lower. Try again!'
    elif guess > riddle_num:
        return 'Your number is higher. Try again!'
    return True


def create_random_number(border):
    random_number = randint(1, border)
    return random_number


def exit_game():
    print(f'Number of attempts: {counter}')
    print('Bye')
    exit()


counter = 0


def game():
    global counter
    counter = 0
    border_num = input('Enter right border number or "q" to quit game: ')
    border_num = is_valid(border_num)
    riddle = randint(1, border_num)
    # print(riddle)
    while True:
        guess_num = is_valid(
            input(f'Take a guess between one and {border_num} '))
        counter += 1
        check = check_guess(guess_num, riddle)
        if check is True:
            print(f'Correct! Number of attempts: {counter}')
            ask = input('Play again? Press "Y" to continue or any other key to quit')
            if ask.lower() == 'y':
                game()
            else:
                exit_game()
        else:
            print(check)


if __name__ == "__main__":
    game()

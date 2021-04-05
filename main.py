def hello(bot_name, year):
    print("Hello! My name is " + bot_name)
    print("I was created in " + year)


def name():
    print("Please, remind me your name.")
    user_name = input()
    print("What a great name you have, " + user_name + "!")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count_number():
    print('Now I will prove to you that I can count to any number you want.')
    number = int(input())
    count = 0
    while count <= number:
        print(str(count) + " " + "!")
        count += 1


def knowledge():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    correct_answer = 2
    answer = int(input())

    while answer != correct_answer:
        print("Please, try again.")
        answer = int(input())


def congratulations():
    print("Completed, have a nice day!")
    print("Congratulations, have a nice day!")


hello("Aid", "2020")
name()
guess_age()
count_number()
knowledge()
congratulations()
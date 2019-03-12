import random

def guess_number():
    users_name = str(input("What is your username? "))
    users_number = int(input("Hi " + users_name + ", I am thinking of a number between 1-100, what do you think that number is?\n "))
    correct_number = random.randint(1,100)
    users_tries = []
    users_tries.append(users_number)

    while users_number != correct_number:
        if users_number > correct_number:
            users_number = int(input("Sorry, that answer was too high! Try again!\n "))
            #correct_number = guess_number + 1
            if users_number not in users_tries:
                users_tries.append(users_number)
        if users_number < correct_number:
            users_number = int(input("Sorry, that answer was too low! Try again!\n "))
            #correct_number = guess_number + 1
            if users_number not in users_tries:
                users_tries.append(users_number)

    if users_number not in users_tries:
        users_tries.append(give_number)
    print ("Congratulations " + users_name + ", you got it right! The answer was: " + str(correct_number) + " it took you " + str(len(users_tries)) + " tries!")




guess_number()

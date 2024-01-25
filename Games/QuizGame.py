def new_game():
    guesses = []
    correct_guessses = 0
    ques_num = 1

    for key in questions:
        print(key)
        for i in options[ques_num - 1]:
            print(i)
        ques_num += 1
        guess = input("Enter option: ").upper()
        guesses.append(guess)

        if check_answer(questions.get(key), guess):
            correct_guessses += 1

    display_score(correct_guessses, guesses)


    print("----------------------------------------------------------")
#---------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!!!!")
        return True
    else:
        print("WRONG!!!!")
        return False
#---------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------------------------------------")
    print("Your score is: ")
    print("----------------------------------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100 )
    print("u r score is: " + str(score) + "%")


#---------------------------
def play_again():
    res = input("Do u wanna play again(Y/N)?: ").upper()
    if res.startswith("Y"):
        return True
    else:
        return False
#---------------------------



questions = {
    "Who created Python?:" : "A",
    "When was Python created?:" : "B",
    "Python is linked with which comedy group?:" : "C",
    "Is earth round?:" : "A"
}

options = [["A. Guido van Rossum", "B. Elon", "C. Bill", "D. Mark"],
           ["A. 1992", "B. 1991", "C. 1852", "D. 1963"],
           ["A. Island", "B. BigBang", "C. Monty Python", "D. Frnds"],
           ["A. True", "B. Maybe", "C. False", "D. Can't guess"]]


new_game()
while play_again():
    new_game()

print("Have a nice day")
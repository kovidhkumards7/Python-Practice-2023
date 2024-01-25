import random

RPS = ["Rock","Paper","Sissor"]
game = True
while game:
    comp = random.choice(RPS)
    try:
        while True:
            user = input("Rock,Paper,Sissor\nEnter ur choice: ")
            if user in RPS:
                break
        comp = comp.lower()
        user = user.lower()
        if comp == user:
            print("U r choice is:",user)
            print("computer choice is: ",comp)
            print("it is a tie")
        elif comp == "Rock" and user == "Paper":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U win")
        elif comp == "Rock" and user == "Sissor":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U lose")
        elif comp == "Paper" and user == "Sissor":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U win")
        elif comp == "Paper" and user == "Rock":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U lose")
        elif comp == "Sissor" and user == "Rock":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U win")
        elif comp == "Sissor" and user == "Paper":
            print("U r choice is:", user)
            print("computer choice is: ", comp)
            print("U lose")
        res = input("Wanna play again(y/n): ")
        if res == "n":
            game = False
    except:
        print("err occured")
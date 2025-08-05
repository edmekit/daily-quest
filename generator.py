import random

print("Good day to you.")

ans = input("Let's generate our quests for the day? ").capitalize()
if ans == "Yes":
    with open("quests.txt", "r", encoding="utf-8") as q:
        quests = q.readlines()
    ques = []

    for quest in quests:
        ques.append(quest)

    print("Here is your quest for today: ", end="")
    print(random.choice(ques))

else:
    print()
    print("Goodbye and good luck to you.")
    SystemExit


    


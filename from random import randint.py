from random import randint

tools = ["rock", "scissors", "paper"]
results = {("scissors", "paper"): "scissors",
("paper", "rock"): "paper",
("scissors", "rock"): "rock"}


user_choice = input("rock, paper scissors:")
if user_choice not in tools:
    raise Exception("nie wybrano nic")

comp_choice = tools[randint(0, 2)]
print(comp_choice)
if user_choice == comp_choice:  
    print("(ㆆ_ㆆ)")
else:
    for result in results:
        if user_choice in result and comp_choice in result:
            winner = results[result]
            if user_choice == winner:
                print("dobre to było") 
            else:
               print("ale ez z tobą")
               break                    # Dominik kuhler i Wojciech Kacprzak
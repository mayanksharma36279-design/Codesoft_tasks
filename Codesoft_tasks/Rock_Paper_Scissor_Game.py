import random

choices = ["rock", "paper", "scissor"]
score_of_user = 0
computer_score = 0

print("ROCK PAPER SCISSOR GAME")

while True:
    user_choice = input("Choose Rock, Paper or Scissor: ").lower()

    if user_choice not in choices:
        print("Invalid Choice, try again")
        continue

    computer_choice = random.choice(choices)

    print(f"You choose : {user_choice}")
    print(f"Computer choose : {computer_choice}")

    if user_choice == computer_choice:
        print("Game is Tied")

    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You Won")
        score_of_user += 1

    else:
        print("Computer Won")
        computer_score += 1

    print(f"Your Score: {score_of_user} | Computer Score: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thanks for Playing")
        break

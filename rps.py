import random

# Mapping choices with numbers, names, and hand signs
choices = {
    1: ("Rock", "✊"),
    2: ("Paper", "✋"),
    3: ("Scissors", "✌️")
}

def get_user_choice():
    print("\nChoose your option:")
    print("1 - Rock ✊")
    print("2 - Paper ✋")
    print("3 - Scissors ✌️")

    choice = input("Enter your choice (1/2/3): ")
    while choice not in ["1", "2", "3"]:
        print("Invalid input. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ")

    return int(choice)

def show_choice(name, sign, player="You"):
    print(f"{player} chose: {name} {sign}")

def determine_winner(user, computer):
    user_name, user_sign = choices[user]
    comp_name, comp_sign = choices[computer]

    show_choice(user_name, user_sign, "You")
    show_choice(comp_name, comp_sign, "Computer")

    if user == computer:
        return "🤝 It's a tie!"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors with Emojis!")
    while True:
        user_choice = get_user_choice()
        computer_choice = random.randint(1, 3)

        print("\n🕹️ Game Result:")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        while play_again not in ["y", "n"]:
            play_again = input("Please enter only 'y' to continue or 'n' to exit: ").lower()

        if play_again == "n":
            print("👋 Thanks for playing!")
            break

play_game()
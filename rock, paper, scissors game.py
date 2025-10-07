import random

choices = ["rock", "paper", "scissors"]
command = ""

while command != "quit":
    command = input("Type something (or 'quit' to stop): ")
    print("You typed:", command)

    if command == "quit":
        break

    user_choice = input("Enter your choice (rock/paper/scissors): ")
    print("Your choice was:", user_choice)

    computer = random.choice(choices)
    print("Computer's choice was:", computer)

    if user_choice == computer:
        print("Tie!")
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "scissors" and computer == "paper") or \
         (user_choice == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thank you for playing!")
        break

input("Press Enter to exit.")


                 
        

             

         
          

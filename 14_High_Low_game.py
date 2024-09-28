import random  # Import the random module to generate random numbers

# Constants
TOTAL_ROUNDS = 5  # Define the total number of rounds for the game

def play_high_low_game():
    print("Welcome to the High-Low Game!")  # Welcome message
    print("--------------------------------")

    player_score = 0  # Initialize the player's score

    # Loop through each round of the game
    for current_round in range(1, TOTAL_ROUNDS + 1):
        # Generate random numbers for player and computer
        player_value = random.randint(1, 100)  # Player's number
        computer_value = random.randint(1, 100)  # Computer's number

        print(f"\nRound {current_round}")  # Display the current round number
        print(f"Your number is: {player_value}")  # Show the player's number
        
        # Get the player's guess
        user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        # Validate user input until it is either 'higher' or 'lower'
        while user_guess not in ['higher', 'lower']:
            print("Invalid input. Please enter 'higher' or 'lower'.")  # Error message for invalid input
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        # Game logic to determine if the guess is correct
        if (user_guess == 'higher' and player_value > computer_value) or (user_guess == 'lower' and player_value < computer_value):
            print("You were right! The computer's number was:", computer_value)  # Correct guess
            player_score += 1  # Increment score
        elif player_value == computer_value:
            print("It's a tie! The computer's number was:", computer_value)  # Handle tie situation
        else:
            print("Aww, that's incorrect. The computer's number was:", computer_value)  # Incorrect guess

        print(f"Your score is now: {player_score}")  # Display current score

    # Game over; display final score and message
    print("\nThanks for playing!")
    display_final_score_message(player_score)  # Call function to display final score message

def display_final_score_message(score):
    # Provide feedback based on the final score
    if score == TOTAL_ROUNDS:
        print("Perfect score! You guessed everything right!")  # Perfect score message
    elif score > TOTAL_ROUNDS / 2:
        print("Good job, you played really well!")  # Above average message
    else:
        print("Better luck next time!")  # Below average message

# Start the game
play_high_low_game()  # Call the function to initiate the game

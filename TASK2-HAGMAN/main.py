import random
from hangman_words import word_list
from hangman_art import logo, stages
def play_hangman():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    print("Welcome To Hangman!!!")
    print(logo)

    # Create blanks
    display = ["_"] * word_length
    guessed_letters = []

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
        else:
            guessed_letters.append(guess)

            # Check guessed letter
            if guess in chosen_word:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")
                    print(f"The correct word was: {chosen_word}")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has won
        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(stages[lives])

# Main game loop
while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#without yes or no 
# import clear
# import random
# from hangman_words import word_list
# from hangman_art import logo, stages
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# end_of_game = False
# lives = 6
#
#
# print("Welcome To Hangman!!!")
# print(logo)
# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     #clear()
#     if guess in display:
#         print(f"You've already guessed {guess}")
#     # Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     # Check if user is wrong.
#     if guess not in chosen_word:
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#             print(f"Finally the Correct word is **{chosen_word}**")
#
# # Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     # Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     print(stages[lives])
#


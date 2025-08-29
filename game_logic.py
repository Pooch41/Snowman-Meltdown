import random
import ascii_art as aa

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage for the current number of mistakes."""
    print("-" * 75) #prints break line for clarity
    print(aa.STAGES[mistakes])
    if mistakes != len(aa.STAGES[mistakes]):
        display_word = ""
        guessed_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
                guessed_word += letter
            else:
                display_word += "_ "
        print("Word: ", display_word)
        print("\n")
        return guessed_word
    return None


def play_game():
    """Main gameplay loop logic. Player inputs single letter as guess.
    Depending on result, either deduct life or not, make next guess.
    After game is done, ask if replay y/n."""
    while True:
        mistakes = 0
        secret_word = get_random_word()
        print("""Welcome to Snowman Meltdown!
            Guess the word, letter by letter, do it right, or the snowman melts!""")
        guessed_letters = []
        guessed_word = ""

        while True:

            guessed_word = display_game_state(mistakes, secret_word, guessed_letters)

            if guessed_word == secret_word: #break out before displaying snowman again, player wins
                print("You have saved the snowman!")
                break

            if mistakes == (len(aa.STAGES) - 1): #Only hat left of the snowman, player loses
                print("The snowman has melted!")
                break

            while True:
                    guess = input("Guess a letter: ").lower()
                    if len(guess) == 1 and guess.isalpha(): #check if it's one letter exactly
                        break
                    print("Please enter one letter!")

            if guess in secret_word:
                guessed_letters.append(guess)
            else:
                mistakes += 1

        while True: #prompt if player wants to play again
            replay = input("Play again? (y/n): ").lower()
            if replay == "y" or replay == "n":
                break
            print("Please enter 'y' or 'n'!")

        if replay == "n":
            print("Exiting, goodbye!")
            break


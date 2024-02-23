import random
import stage

print("Welcome to Hangman, a word will be randomly chosen and you must guess letters one at a time, Goodluck!")
wordList = [
    "Elephant", "Sunshine", "Galaxy", "Bicycle", "Mountain", "Whisper", "Pizza", "Moonlight", "Jellybean", "Ocean",
    "Feather", "Laptop", "Dragonfly", "Rainbow", "Pineapple", "Thunder", "Marshmallow", "Telescope", "Tornado",
    "Lighthouse", "Espresso", "Balloon", "Avalanche", "Waterfall", "Galaxy", "Firefly", "Cookie", "Hummingbird",
    "Bumblebee", "Butterfly", "Stardust", "Aurora", "Cinnamon", "Popsicle", "Dandelion", "Starfish", "Chocolate",
    "Unicorn", "Jellyfish", "Fireworks", "Lemonade", "Seashell", "Bubblegum", "Mountain", "Blizzard", "Sandcastle",
    "Rainbow", "Mermaid", "Whirlwind", "Blueberry", "Adventure", "Moonbeam", "Hurricane", "Sushi", "Shooting",
    "Tangerine", "Avalanche", "Watermelon", "Bubble", "Symphony", "Marshmallow", "Dragonfly", "Firecracker",
    "Espresso", "Carousel", "Galaxy", "Bonfire", "Waterfall", "Chocolate", "Sunshine", "Lemonade", "Butterfly",
    "Thunderstorm", "Sandcastle", "Rainbow", "Bumblebee", "Stardust", "Lighthouse", "Seashell", "Pineapple",
    "Blizzard", "Jellybean", "Moonlight", "Bicycle", "Whisper", "Popsicle", "Dragonfly", "Hurricane", "Tornado",
    "Unicorn", "Aurora", "Symphony", "Adventure", "Espresso", "Balloon", "Bubblegum", "Dandelion", "Cookie",
    "Galaxy", "Moonbeam"
]

chosenWord = random.choice(wordList).lower()  # Select a random word and convert it to lowercase
spaces = len(chosenWord)
linesList = ['_' for _ in range(spaces)]  # Create a list of underscores representing the hidden word

print("Your word:", linesList)
guesses = [] #list to keep track of user guess
gameStatus = '' #string for updating game status
lives = 6 #initial live count

#game loop while game is not finished
while gameStatus != 'Game Over':
    userGuess = input("Guess a letter: ").lower()
    if userGuess in guesses:
        print("You have already guessed this, pick a new letter!")

    else:
        guesses.append(userGuess)
        if userGuess in chosenWord:  # If the guessed letter is in the chosen word
            for i, char in enumerate(chosenWord):
                if char == userGuess:
                    linesList[i] = userGuess
            print("Correct Guess:", linesList)
            print(stage.stages[lives])
            print(f"User Guesses: {guesses}")
        else:  # If the guessed letter is not in the chosen word
            lives -= 1
            print(f"Word: {linesList}")
            print("Incorrect Guess.", stage.stages[lives])
            print(f"User Guesses: {guesses}")
            if lives == 0:
                gameStatus = 'Game Over'
                print("You ran out of lives! Game Over.")
                break

        if '_' not in linesList:  # If there are no more underscores left in the word
            gameStatus = 'Game Over'
            print("Congratulations! You guessed the word:", chosenWord)
            break
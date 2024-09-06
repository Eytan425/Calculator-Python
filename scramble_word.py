import random

def scramble_word(word):
    """Scramble the letters of the word."""
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ['python', 'algorithm', 'function', 'variable', 'loop', 'dictionary']
    word_to_guess = random.choice(words).lower()
    scrambled_word = scramble_word(word_to_guess)
    return scrambled_word, word_to_guess
    
def Game():
    attempts = 10
    scrambled_word, word_to_guess = word_scramble_game()
    print(scrambled_word)  # Show the scrambled word
    guess = input("Guess the word: ")
    
    while guess != word_to_guess:
        attempts -= 1
        if attempts != 0:
            print(f"Wrong guess! You have {attempts} attempts left.")
            guess = input("Guess the word: ")
        else:
            print("You ran out of attempts!")
            print("You will get it next time!")
            return f"The word was '{word_to_guess}'"
    
    return "You guessed it!"

print(Game())

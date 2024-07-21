from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()  # Ensure the word is uppercase
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user
    attempts = 6  # Number of allowed wrong attempts

    while word_letters and attempts > 0:
        print("Used letters:", ' '.join(sorted(used_letters)))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", ' '.join(word_list))
        #Get User Input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                attempts -= 1
                print(f"Incorrect. You have {attempts} attempts left.")
        elif user_letter in used_letters:
            print("You have already guessed that letter. Please try a different one.")
        else:
            print("Invalid character. Please enter a letter.")

    if not word_letters:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over. The word was:", word)

hangman()

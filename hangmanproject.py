# import random to randomly pick word
import random
# from the python file chosen i will import a list
from words import wordlist
from countries import countries
from sports import sportslist


def get_word():
    word = random.choice(wordlist)
    return word.upper()


def get_country():
    country = random.choice(countries)
    return country.upper()


def get_sports():
    sports = random.choice(sportslist)
    return sports.upper()


# Use this method if the user choose to play countries
def play(country):
    country_completion = "_" * len(country)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("THE HANGMAN GAME")
    print(display_hangman(tries))
    print(country_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a country: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in country:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well Done,", guess, "is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(country_completion)
                indices = [i for i, letter in enumerate(country) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                country_completion = "".join(word_as_list)
                if "_" not in country_completion:
                    guessed = True
        elif len(guess) == len(country) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != country:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                country_completion = country
        else:
            print("Invalid guess.")
        print(display_hangman(tries))
        print(country_completion)
        print("\n")
    if guessed:
        print("Congratulations :) , you have guessed the word! You win!!!!!!")
    else:
        print("Sorry, you ran out of tries :(  The word was " + country + ". Try again next time :( ")


# Use this method if the user choose to play  animals
def play(word):
    finishedword = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("THE HANGMAN GAME")
    print(display_hangman(tries))
    print(finishedword)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well Done,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(finishedword)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                finishedword = "".join(word_as_list)
                if "_" not in finishedword:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                finishedword = word
        else:
            print("Invalid guess.")
        print(display_hangman(tries))
        print(finishedword)
        print("\n")
    if guessed:
        print("Congratulations :) , you have guessed the word! You win!!!!!!")
    else:
        print("Sorry, you ran out of tries :(  The word was " + word + ". Try again next time :( ")


# Use this method if the user choose to play  sports
def play(sports):
    finishedword = "_" * len(sports)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("THE HANGMAN GAME")
    print(display_hangman(tries))
    print(finishedword)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in sports:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well Done,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(finishedword)
                indices = [i for i, letter in enumerate(sports) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                finishedword = "".join(word_as_list)
                if "_" not in finishedword:
                    guessed = True
        elif len(guess) == len(sports) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != sports:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                finishedword = sports
        else:
            print("Invalid guess.")
        print(display_hangman(tries))
        print(finishedword)
        print("\n")
    if guessed:
        print("Congratulations :) , you have guessed the word! You win!!!!!!")
    else:
        print("Sorry, you ran out of tries :(  The word was " + sports + ". Try again next time :( ")


# stages for every incorrect letter
def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   |
                  ----
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   |
                  ----
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   |
                  ----
                """,


                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   |
                  ----
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   |
                  ----
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   |
                  ----
                """
    ]
    return stages[tries]


def main():
    # Show menu #
    print(30 * "-")
    print("   M A I N - M E N U")
    print(30 * '-')
    print("Categories ")
    print("1. Countries")
    print("2. Animals")
    print("3. Sports")
    print(30 * '-')
    # Get input #
    choice = input("Enter your choice [1-3] : ")

    # Convert string to int type #
    choice = int(choice)

    # countries = ["Nigeria", "England", "Ghana","Scotland","Wales","USA"]
    # animals = ["cat", "dog", "eagle"]
    # sports = ["football", "hockey", "tennis"]

    # Take action as per selected menu-option #
    if choice == 1:
        print("Countries category ---> ")
        country = get_country()
        play(country)
        while input("Play Again? (Y/N) ").upper() == "Y":
            country = get_country()
            play(country)
    elif choice == 2:
        print("Animal category --->")
        word = get_word()
        play(word)
        while input("Play Again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)

    elif choice == 3:
        print("Sports Category --->")
        sports = get_sports()
        play(sports)
        while input("Play Again? (Y/N) ").upper() == "Y":
            sports = get_sports()
            play(sports)
    else:
        print("Invalid number. Try again...")
    """   
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
    """


if __name__ == "__main__":
    main()

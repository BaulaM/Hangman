word = "Beeeeeem"
def length_string(string) -> int:
    count = 0
    for letter in string:
        count += 1
    return count

def hangman_game(word):
    word = word.lower()
    attempts = 5
    sucesses = 0
    correct_guess=""
    word_len = length_string(word)

    while attempts > 0 and sucesses < word_len:
    #Ensuring user input is valid
        val = input(" :Enter letter ->")
        if len(val) == 1 and val.isalpha():
            print("Youve entered : " + val)
        else:
            print("Input error, must be a single letter")
            continue

    #keeping track of user progression
        if val.lower() in word:
            sucesses += word.count(val.lower())
        else:
            attempts -= 1
            print(f"Incorrect: {attempts} tries left")

        if attempts == 0:
            print("you have failed")

    #Filling in correct guesses
        correct_guess +=  val.lower()

        for letter in word:
            if letter.lower() in correct_guess:
                print(letter.lower(), end="")
            else:
                print("_", end="")

    if sucesses == word_len:
        print("")
        print("Congratulations, you have won!")
hangman_game(word)

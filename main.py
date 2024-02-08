from wonderwords import RandomWord

r = RandomWord()


Hp = 10  # Guesses
letters_found = ""
# start
# execute the random word selection - and run game

word_chosen = r.word()
run_game = True

word = []

blanks = []

###########################
for letter in word_chosen:
    word.append(letter)

for letter in word:
    blanks.append("_")
##########################


# loop :)
while run_game:

    print("This word has", len(word_chosen), "letter's", blanks, ", you have", Hp, "guesses")
    enter_guess = input("Please guess 1 letter:")
    if len(enter_guess) <= 1 or not enter_guess.isdigit():
        if enter_guess in word_chosen:

            if enter_guess not in letters_found or word_chosen.lower().count(
                    enter_guess) != letters_found.lower().count(enter_guess):

                # gets blanks, prob put vars at top, but i'm too lazy
                leg = len(word)
                i = 0
                how_may_correct = 0
                while i < leg:
                    if enter_guess == word[i]:
                        blanks[i] = enter_guess

                        how_may_correct = how_may_correct + 1
                    i += 1
                print(blanks)
                print(how_may_correct, "correct!")
        else:
            Hp -= 1
            print("Incorrect! You now have", Hp, "Guesses")
            if Hp <= 0:
                print("You lost :(")
                print("The word was", word_chosen)
                print("Game over")
                run_game = False

    elif len(enter_guess) >= 1 or enter_guess.isdigit():
        print("Cannot input numbers or more than 1 letter")

    enter_guess = ""
    print(letters_found)
    if "_" not in blanks:
        print("Word Found!")
        run_game = False

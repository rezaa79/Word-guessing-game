import random

def save_words(words):
    with open("words.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

def choose_random_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
        random_word = random.choice(words).strip()
        return random_word


input_words = input("word_list: ")
words_list = input_words.split(",")


save_words(words_list)


random_word = choose_random_word()
print("random_word: " + random_word)



correct_guesses = []
wrong_guesses = []
chances = 5

while chances > 0:
    letter = input("input your word: ")
    
    if letter in random_word:
        correct_guesses.append(letter)
        print("Words guesses correctly: " + ", ".join(correct_guesses))
    else:
        wrong_guesses.append(letter)
        chances -= 1
        print("Wrong words guessed: " + ", ".join(wrong_guesses))
        print("Number of chances left: " + str(chances))
    
    if set(correct_guesses) == set(random_word):
        print("Congratulations, you got it right.")
        print("The right word: " + random_word)
        break

if chances == 0:
    print("sorry, you are out of luck. the right word: " + random_word)

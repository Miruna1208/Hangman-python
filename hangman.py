import random

word_list = [
    "apple", "banana", "orange", "grape", "cherry",
    "computer", "keyboard", "python", "hangman", "laptop",
    "elephant", "giraffe", "kangaroo", "dolphin", "tiger",
    "school", "teacher", "student", "library", "university",
    "mountain", "river", "forest", "desert", "ocean"
]

secret_word = random.choice(word_list)

print("Your secret word: ")

secret_word_letters = [];
secret_word_lines = [];
for char in secret_word:
    secret_word_letters.append(char)
    secret_word_lines.append("_")

print(''.join(secret_word_lines))

word_found = 0

while(not word_found):
    print("Type your guess: ")
    letter = input()
    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word_letters[i] == letter:
                secret_word_lines[i] = letter
        print(''.join(secret_word_lines))

    elif letter not in secret_word:
        print("not ok")





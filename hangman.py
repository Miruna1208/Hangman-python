import random

word_list = [
    "apple", "banana", "orange", "grape", "cherry",
    "computer", "keyboard", "python", "hangman", "laptop",
    "elephant", "giraffe", "kangaroo", "dolphin", "tiger",
    "school", "teacher", "student", "library", "university",
    "mountain", "river", "forest", "desert", "ocean"
]

hangman = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]

secret_word = random.choice(word_list)

secret_word_letters = [];
secret_word_lines = [];
for char in secret_word:
    secret_word_letters.append(char)
    secret_word_lines.append("_")

count_mistakes = 0;
used_letters = [];

while(True):
    print("Type your guess(used letters: "+ ' '.join(used_letters) + ")")
    print(''.join(secret_word_lines))
    letter = input()
    if letter not in used_letters:
        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word_letters[i] == letter:
                    secret_word_lines[i] = letter
            print(''.join(secret_word_lines))
            if "_" not in secret_word_lines:
                print("You won! :)")
                break
        elif letter not in secret_word:
            count_mistakes += 1
            if count_mistakes != 7:
                print(hangman[count_mistakes])
            else:
                print("You lost :|")
                print("The word is: " + secret_word)
                break
        used_letters.append(letter)
    else:
        print("You already used this letter! ")
        

        
        





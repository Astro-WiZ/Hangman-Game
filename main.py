import random
import hangman_art
import hangman_words
# word_list = ["apple", "breakdown", "ubuntu","kalilinux"]

# Pick a random letter from word list
#word_index = random.randint(0,len(word_list)-1)
#chosen_word = word_list[word_index]
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)

print(chosen_word)
display=[]
for _ in range(word_len):
  display += ["_"]
print('  '.join(display))

# ask user to guess the letter and assign to variable guess. Make guess Lowercase


#check the guess letter is one of the letter in the word
end_of_game = False
lives = 6
while not end_of_game:
  guess = input("Guess a letter in word : ").lower()

  #display if the letter is already entered
  
  if guess in display:
    print(f"You already entered the letter {guess}.")

  # for guess n
      

  for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
      
  print('  '.join(display))
  
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}. That's not in the word. You lose a life")
    if lives == 0:
      end_of_game = True
      print("You Lose!")

  print(hangman_art.stages[lives])

  
  if "_" not in display:
    end_of_game = True
    print("You Win the game!")
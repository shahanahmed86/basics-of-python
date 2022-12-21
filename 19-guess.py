secret_word = 'giraffe'
guess_count = 0
guess_limit = 3
guess = ''

while guess != secret_word:
  if (guess_limit == guess_count):
    print('Out of guesses, you\'ve lost the game!!!')
    break
  guess = input('Guess: ')
  guess_count += 1
else:
  print('You\'ve won the game!!!')

print('EndGame!!!')
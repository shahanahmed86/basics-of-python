is_male = False
is_tall = False

if is_male and is_tall:
  print('You\'re a tall male')
elif is_male and not is_tall:
  print('You\'re not a tall male')
elif not is_male and is_tall:
  print('You\'re tall but not a male')
else:
  print('You\'re neither male nor tall')
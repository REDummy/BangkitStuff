def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character.
  for i in range(len(text)) :
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if text[i].isdigit() :
      # Complete the if-statement using a logical operator to check if
      # the number is not already in the dictionary.
      if text[i] not in dictionary:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           dictionary.update({text[i] : 1})
      else:
          dictionary[text[i]] += 1
      # Use a dictionary operation to increment the number count value
      # for the existing key.
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}
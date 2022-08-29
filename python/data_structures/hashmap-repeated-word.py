

# Write a function called repeated word that finds the first word to occur more than once in a string

def repeated_word(sample_string):
# split the sample string
# create a for loop to read each word in the string
  # get the current word
  # check to see if the current word is in the dictonary
  # if its in the dict
    # return the word being checked
  # if its not in the dect
    # add word (key) and value(count) to the dict

  split_string = sample_string.split() #"Once upon a time, a brave princess who..."
  # print(split_string)
  dict = {}
  for word in split_string:
    if word in dict:
      return word
    if word not in dict:
      dict[word] = 1
  return "No repeated word"

print(repeated_word("Once upon a time, a brave princess who..."))



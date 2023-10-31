with open("./books/frankenstein.txt") as f:
  file_contents = f.read()

def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  char_dict = {}
  for char in text.lower():
    if(char in char_dict):
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return char_dict

def report(text):
  word_count = count_words(text)
  char_dict = count_characters(text)
  char_list = list(char_dict.items())
  char_list.sort()

  print(f"\n--- Begin report of books/frakenstein.txt")
  print(f"{word_count} words found in the document\n")

  for char in char_list:
    if(char[0].isalpha()):
      print(f"The '{char[0]}' character was found {char[1]} times")

  print(f"--- End report ---\n")



report(file_contents)
# count_characters(file_contents)

# count_words(file_contents)
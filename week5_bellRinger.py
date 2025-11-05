# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
first_occurence_c = magic.find('c')
print(first_occurence_c)

# Advanced Slicing:
# Given the string 
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
every_second_letter=alphabet[0:13:2]
# c. Reverse the entire string using slicing.
reversed_alphabet = alphabet [::-1]
print(reversed_alphabet)
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the 
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find('John F. Kennedy'))
personality_name=quote[78:]
print(personality_name)

# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.rfind('subjective'))
subjective_word=info[36:]
print(subjective_word)
# b. Extract every third word.
every_third_word= info.split()[::3]
print(every_third_word)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_string =every_third_word[::-1]
print(reversed_string)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase:"MAY THE FORCE BE WITH YOU."
uppercase_statement = "MAY THE FORCE BE WITH YOU."
print("Lowercase:", uppercase_statement.lower())

# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
single_string = ' '.join(motto)
print(single_string)
# b. Now, split the string at every occurrence of the letter 'a'.
split_string=single_string.split('a')
print(split_string)


# Replacing Words:
# Modify the 
sentence= "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
new_text = sentence.replace("busy","distracted")
print(new_text)
# b. Replace "plans" with "mistakes".
new_text = sentence.replace("plans","mistakes")
print(new_text)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
word_one="Iteration "
result=word_one * 7
print(result)

# Word Search:
# Check if the word 
# "moonlight" appears in the 
quote_three = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_two = "moonlight"

if "moonlight" in quote_three:
  print("The word 'moonlight' appears in the quote.")
else:
  print("The word 'moonlight' does not appear in the quote.")


# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase_super = "Supercalifragilisticexpialidocious"
length_of_phrase= len(phrase_super)
# b. Count the number of times the letter 'i' appears in the same word/phrase.
count_i = phrase_super.count('i')
(print(count_i))
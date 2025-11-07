def problem_set2():
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from th
    quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote.find('John F. Kennedy'))
    personality_name =quote[78:]
    print(personality_name)
    # Manipulating words:
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
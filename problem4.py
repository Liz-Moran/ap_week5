def problem_set4():
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
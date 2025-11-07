def problem_set3():
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
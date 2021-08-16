print("Enter a character to check: ", end="")

random_character, lowercase, uppercase = str(input()), 0, 0


if (random_character and random_character.isalpha()):


    lowercase = random_character == 'a' or random_character == 'e' or random_character == 'i' or random_character == 'o' or random_character == 'u'
    
  
    uppercase = random_character == 'A' or random_character == 'E' or random_character == 'I' or random_character == 'O' or random_character == 'U'
    
    if (lowercase or uppercase):
        print("\n'", random_character, "' is a vowel character.")
    else:
        print("\n'", random_character, "' is a consonant character.")
else:
    print("\nSorry, You entered a Non-Alphabetic character!")
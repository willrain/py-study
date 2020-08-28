
original = input("Enter a word: ")

if len(original) > 0 and original.isalpha():
    # do your job
    first_char = original[0]
    new_word = original[1:] = first_char + 'ay'
    print(new_word)
else:
    print('invalid word')




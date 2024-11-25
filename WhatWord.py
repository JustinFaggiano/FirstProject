import itertools

# Load a word list from a dictionary file (e.g., words in English)
# You can download a word list and save it as 'words.txt' in the same directory as this script
with open('words.txt') as f:
    word_list = set(f.read().split())

def find_words(input_word):
    input_word = input_word.lower()
    found_words = set()
    
    # Generate permutations of the word's letters for all lengths
    for i in range(1, len(input_word) + 1):
        for perm in itertools.permutations(input_word, i):
            possible_word = ''.join(perm)
            if possible_word in word_list:
                found_words.add(possible_word)
                # Stop if we reach 10 words
                if len(found_words) == 10:
                    return found_words
    
    return found_words

# Ask the user for input
user_input = input("Enter a word: ").strip()
result_words = find_words(user_input)

if result_words:
    print("Here are some words you can make with the letters:")
    for word in result_words:
        print(word)
else:
    print("No words could be made from the letters of your input.")

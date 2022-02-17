def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("FAIL")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename, searchWord):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("FAIL")
        pass
    else:
        searchWord = searchWord.lower()
        contents = contents.lower()
        numTimes = contents.count(searchWord)
        print(f"The word {searchWord} occured {numTimes} times in the file {filename}")
        
        


searchWord = input("What word would you like to search for? ")
filenames = ['Chapter10/Augustus.txt', 'Chapter10/Bacon.txt', 'Chapter10/The_Last_Plunge.txt']
for filename in filenames:
    count_words(filename)
for filename in filenames:
    find_words(filename, searchWord)

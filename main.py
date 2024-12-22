import string

def main():
    print("Path to the file:")
    file_path = input()
    
    print_report(file_path)

#function that counts words in the text
def count_words(x):  

    word_list = x.split()

    return len(word_list) 

#function that counts the characters and sort them descending
def count_characters(x):
    char_list = list(x.lower())

    lower_alpha_list = list(string.ascii_lowercase)
    
    character_count = {}

    for i in lower_alpha_list:
        x = char_list.count(i)
        if x != 0:
            character_count[i] = x
    
    return dict(sorted(character_count.items(), key=lambda item:item[1], reverse=True))


#function that prints the report
def print_report(file_path):
    print(f"--- Begin report of {file_path}")
    
    with open(file_path) as f:
        file_contents = f.read()

    counted_words = count_words(file_contents)

    print(f"{counted_words} words found in the document")
    print("")

    counted_characters = count_characters(file_contents)

    for char in counted_characters:
        print(f"The {char} character was found {counted_characters[char]} times")

    print("--- End report ---")

main()
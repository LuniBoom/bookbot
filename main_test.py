def main():
    text = get_book_text()
    wrd_count = word_count(text)
    char_count = character_count(text)
    char_report = character_report(char_count)

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count(text):
     words = text.split()
     print(len(words))
     return len(words)

def character_count(text):
    characters = {}
    for char in text.lower():
        if char not in characters:
            characters[char] = 1
        elif char in characters:
            characters[char] += 1
    print(characters)
    return characters

def character_report(char_count):
    char_list = []
    temp_dict = {}

    for char in char_count:
        if char.isalpha():
            temp_dict[char] = char_count[char]
            char_list.append(temp_dict)
          


main()

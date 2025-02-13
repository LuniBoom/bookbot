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
    return characters

def character_report(char_count):
    char_list = []
    key = None
    for char in char_count:
        if char.isalpha():
            key = char_count[char]
            char_list.append({"letter": f"{char}", "count": key})
    char_list.sort(key=lambda x: x["count"], reverse=True)
    print(char_list)
    return char_list


main()
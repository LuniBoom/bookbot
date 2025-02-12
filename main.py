def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
     words = text.split()
     return len(words)

def character_count(text):
    characters = {}
    for char in text.lower():
        if char not in characters:
            characters[char] = 1
        elif char in characters:
            characters[char] += 1
    return characters

text = main()
print(word_count(text))
character_number = character_count(text)
print(character_number)

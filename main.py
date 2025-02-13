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

def report(character_number):
    for char in character_number:
        if char.isalpha():
            character_list.append(char)
    
character_list = []
text = main()
final_report = report(text)
print(word_count(text))
character_number = character_count(text)
print(character_number)
print(character_list)
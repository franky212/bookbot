def main():
    with open("./books/frankenstein.txt", 'r') as f:
        file_contents = f.read()
        count = count_words(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count} words found in the document\n")
        character_count(file_contents)
        print("\n--- End report ---")
        f.close()

def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for word in text:
        lowercased_word = word.lower()
        for character in lowercased_word:
            if character.isalpha():
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1
    character_list = []
    for character in characters:
        character_list.append({"character": character, "num": characters[character]})
    character_list.sort(reverse=True, key=sort_on)
    report(character_list)

def sort_on(dict):
    return dict["num"]

def report(character_list):
    for dict in character_list:
        print(f"The '{dict["character"]}' character was found {dict["num"]}")

main()
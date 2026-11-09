from pathlib import Path

def get_book_text(path_to_file: str) -> str:
    return Path(path_to_file).read_text()

def word_count(file_contents: str) -> int:
    return len(file_contents.split())

def character_count(file_contents: str) -> dict[str, int]:
    characters = {}
    for letter in file_contents.lower():
        characters[letter] = characters.get(letter, 0) + 1
    return characters

def sort_on(character_tuple: tuple[str, int]) -> int:
    return character_tuple[1]

def chars_dict_to_sorted_list(characters: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(characters.items(), reverse=True, key=sort_on)

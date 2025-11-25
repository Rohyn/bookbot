
def count_words(book_string):
    return len(book_string.split())

def char_count(book_string):
    chars = {}
    book_string = book_string.lower()
    for c in book_string:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] = chars[c] + 1
    return chars

def format_report(chars):
    sorted_list = []
    for char in chars:
        if char.isalpha():
            sorted_list.append({"char": char, "num": chars[char]})
    def sort_on(items):
        return items["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    word_count = get_word_count(book)
    letter_counts = get_letter_count(book)
    sorted_count = sort_letter_count(letter_counts)
    print_report(book_path,word_count,sorted_count)

def print_report(path,words,letters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for letter in letters:
        if letter['letter'].isalpha():
            print(f"The '{letter['letter']}' character was found {letter['count']} times")

def sort_on(d):
    return d["count"]

def sort_letter_count(count_dict):
    letter_list = []
    for ch in count_dict:
        letter_list.append({"letter": ch, "count":count_dict[ch]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(book):
    letter_count_dict = {}
    for letter in book.lower():
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1
    return letter_count_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
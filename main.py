def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = order_dict_by_value(get_chars_count(text))
    print_report(path, num_words, char_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_count(text):
    char_dict = {}
    for word in text:
      lowercase_word = word.lower()
      for char in lowercase_word:
        if char.isalpha() == False:
          continue
        if char in char_dict:
          char_dict[char] += 1
        else:
          char_dict[char] = 1

    return char_dict

def order_dict_by_value(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

def print_report(path, num_words, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for char, count in char_dict.items():
        print(f"The '{char}' character was found {count} times")

    print("--- End of report ---")

main()
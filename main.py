def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    #print(word_count)

    letters = list(file_contents.lower())
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    #print(letter_count)

    report = list()
    for lc in letter_count:
        if lc.isalpha() == True:
            report.append(f"The {lc} character was found {letter_count[lc]} times")
    report.sort()


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for line in report:
        print(line)
    print("--- End report ---")

main()
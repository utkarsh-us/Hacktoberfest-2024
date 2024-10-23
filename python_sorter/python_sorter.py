def file_handler(file):
    with open(file, 'r') as f:
        text = f.read()
        words = text.split()
        return words

def separator():
    print(f'\n{"-"*10}\n')

def count_long_words(words, length=10):
    long_words = [word for word in words if len(word) > length]
    print(f'Total words longer than {length} letters: {len(long_words)}')
    print(f'They are: {long_words}')
    separator()

def quick_sort(words):
    if len(words) <= 1:
        return words
    pivot = words[len(words) // 2]
    left = [x for x in words if x < pivot]
    middle = [x for x in words if x == pivot]
    right = [x for x in words if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    file_name = input("Enter the name of the .txt file to process: ")
    words = file_handler(file_name)

    print("Original words:")
    print(words)
    separator()

    sorted_words = quick_sort(words)
    print("Sorted words:")
    print(sorted_words)
    separator()

    count_long_words(words)

if __name__ == "__main__":
    main()